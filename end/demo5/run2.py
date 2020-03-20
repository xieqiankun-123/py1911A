from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
# 配置数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo5.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo5.db'
# 自动检测更新
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        """
        falsk_sqlalchemy的返回对象函数
        :return:
        """
        return self.name


if __name__ == '__main__':
    # 创建表
    # db.create_all()
    # 删除表
    # db.drop_all()
    # 增
    c1 = Category()
    c1.name = "牡丹"
    # c2 = Category()
    # c2.name = "百合"
    db.session.add(c1)
    # db.session.add(c2)
    db.session.commit()
    # 查多个/一个对象
    # cs = Category.query.all()
    # print(cs)
    # c = Category.query.filter_by(id=1)[0]
    # print(c)
    # 修改数据
    # c.name = "红玫瑰"
    # print(c)
    # db.session.commit()
    # 删除数据
    # db.session.delete(c)
    # db.session.commit()




    # app.run()
