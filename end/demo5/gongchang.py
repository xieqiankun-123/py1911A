from flask import Flask, render_template
from views import *
from models import *


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bookbp)
    app.register_blueprint(userbp)
    app.register_blueprint(adminbp)

    @app.before_first_request
    def create_sql():
        print("请求了数据")

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html", error=error)

    # # 配置数据库
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo5.sqlite3'
    app.config["MAIL_SERVER"] = "smtp.163.com"
    app.config["MAIL_PORT"] = 25
    app.config["MAIL_USERNAME"] = "jqk15225767315@163.com"
    app.config["MAIL_PASSWORD"] = "KESIAHIAGIIQCWVS"
    app.config['MAIL_DEFAULT_SENDER'] = '解乾坤大讲堂<15225767315@163.com>'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo5.db'
    # 自动检测更新
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    mail.init_app(app)

    app.secret_key = "}\x8a\x81[?g\xbbF\xc9\xfdA@<|\x1a\x15\x91\xef\x87\xed\xbfel\xa4"
    return app
