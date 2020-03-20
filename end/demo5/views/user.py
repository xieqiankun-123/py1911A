"""
用户蓝图
"""
import email

from flask import Blueprint, request, flash, render_template, redirect, current_app, make_response, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired
from datetime import datetime, timedelta

userbp = Blueprint("user", __name__)


@userbp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        flash({})
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        error = None
        if not email:
            error = "用户名为必填项"
        elif not password:
            error = "密码为必填项"
        if error:
            flash({
                "error": error,
                "email": email,
                "password": password
            })
            return redirect("/login")
        else:
            print(email, password)
            with sqlite3.connect("demo5.db") as con:
                cur = con.cursor()
                cur.execute("select * from user where email = ?", (email,))
                r = cur.fetchall()
                if len(r) > 0:
                    user = r[0]
                    if check_password_hash(user[2], password):
                        if user[5] == 1:
                            next = request.args.get("next")
                            if next:
                                res = make_response(redirect(next))
                                # res.set_cookie("user", email, expires=datetime.now() + timedelta(days=7))
                                session["user"] = email
                                return res
                            else:
                                res = make_response(redirect("/"))
                                # res.set_cookie("user", email, expires=datetime.now() + timedelta(days=7))
                                session["user"] = email
                                return res
                        else:
                            error = "用户未激活，请激活后重新登陆"
                            flash({
                                "error": error,
                                "email": email,
                                "password": password
                            })
                            return redirect("/login")
                    else:
                        error = "密码错误"
                        flash({
                            "error": error,
                            "email": email,
                            "password": password
                        })
                        return redirect("/login")

                else:
                    error = "用户名错误"
                    flash({
                        "error": error,
                        "email": email,
                        "password": password
                    })
                    return redirect("/login")


@userbp.route("/logout", methods=["GET"])
def logout():
    res = make_response(redirect("/"))
    # res.delete_cookie("user")
    session.pop("user")
    return res


@userbp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        error = None
        if not email:
            error = "用户名为必填项"
        elif not password:
            error = "密码为必填项"
        elif not password2:
            error = "重复密码为必填项"
        elif password != password2:
            error = "两次输入密码不一致"
        if error:
            flash(error)
            return redirect("/register")
        else:
            with sqlite3.connect("demo5.db") as con:
                cur = con.cursor()
                cur.execute("select * from user where email = ?", (email,))
                r = cur.fetchall()
                if len(r) > 0:
                    flash("用户名已存在")
                    return redirect("/register")
                else:
                    try:
                        from flask_mail import Message
                        from .uilt import mail
                        password = generate_password_hash(password)
                        cur.execute("insert into user (email , password) values (?,?)", (email, password))
                        cur.execute("select id from user where email = ?", (email,))
                        userid = cur.fetchall()[0][0]
                        sriUtil = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=180)
                        userid = sriUtil.dumps({"userid": userid}).decode("utf-8")
                        from tasks import sendmail
                        sendmail.apply_async((userid, email))
                        con.commit()
                        return redirect("/login")
                    except Exception as e:
                        print(e, "++++")
                        return "出错了"


@userbp.route("/active/<userid>")
def activeuser(userid):
    try:
        sriUtil = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=180)
        userid = sriUtil.loads(userid)
        print(userid)
        with sqlite3.connect("demo5.db") as con:
            cur = con.cursor()
            cur.execute("update user set is_active = 1 where id = ?", (userid["userid"],))
            con.commit()
        return redirect("/login")
    except SignatureExpired:
        return "验证超时"
    except BadSignature:
        return "验证错误，可能时密钥发生错误"
