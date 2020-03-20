"""
视图工具
"""
from flask_mail import Mail
from flask import session, redirect, request
from functools import wraps

mail = Mail()


def checklogin(f):
    @wraps(f)
    def check(*args, **kwargs):
        user = session.get("user")
        if user:
            return f(*args, **kwargs)
        else:
            return redirect("/login?next=" + request.path)

    return check
