from .utils import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        """
        falsk_sqlalchemy的返回对象函数
        :return:
        """
        return self.name


class Book(db.Model):
    # 书记编号
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    # 书籍名称
    name = db.Column(db.String(50), nullable=False, unique=True)

    cid = db.Column("cid", db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    category = db.relationship("Category", backref="books")
