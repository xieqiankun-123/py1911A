from flask import Blueprint, render_template
from models import *

bookbp = Blueprint("book", __name__)


@bookbp.route('/')
def index():
    categoryList = Category.query.all()
    return render_template('index.html', categoryList=categoryList)


@bookbp.route("/category/<id>")
def category_Detail(id):
    print("分类的id为", id)
    category = Category.query.filter_by(id=id)[0]
    bs = category.books
    return render_template("category.html", books=bs)
