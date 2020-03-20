from flask import Blueprint, session, redirect, render_template, request
from models import *
from .uilt import checklogin

adminbp = Blueprint("admin", __name__)


@adminbp.route("/admin")
@checklogin
def admin():
    categorys = Category.query.all()
    return render_template("/admin/admin.html", categorys=categorys)


@adminbp.route("/admin/<resourcetype>/add", methods=["GET", "POST"])
@checklogin
def add(resourcetype):
    resourcetype = resourcetype.capitalize()
    resource = globals()[resourcetype]
    fileds = []
    ps = dir(resource)
    # print(ps)
    for p in ps:
        if (not p.startswith("__")) and (not p.startswith("_")) and (
                p not in ["metadata", "query", "category", "query_class", "books", "id"]):
            fileds.append(p)
    if request.method == "GET":
        return render_template("/admin/add.html", fs=fileds)
    else:
        re = resource()
        re.name = request.form.get("name")
        re.cid = request.form.get("cid")
        # for f in fileds:
        #     re[f] = request.form.get(f)
        # print(re)
        db.session.add(re)
        db.session.commit()
        return redirect("/admin")

    # re = resource()
    # re.name =


@adminbp.route("/admin/<resourcetype>/delete/<id>")
@checklogin
def delete(resourcetype, id):
    print(resourcetype)
    resource = globals()[resourcetype]
    re_obj = resource.query.filter_by(id=id)[0]
    print(re_obj)
    db.session.delete(re_obj)
    db.session.commit()
    return redirect("/admin")
