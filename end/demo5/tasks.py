"""
1.安装celery pip install celery
2.安装python处理redis数据库的驱动 pip install redis
"""
from flask_mail import Message
from views import mail
from celery import Celery
import time, os
from gongchang import create_app

# celery 操作由celery实例开始
app = Celery("tasks", broker="redis://127.0.0.1:6379/10", backend="redis://127.0.0.1:6379/10")
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

tx = create_app()


# 构建任务
@app.task()
def dosomething():
    "耗时任务"
    print("开始执行")
    time.sleep(5)
    print("执行结束")
    return 1000


@app.task()
def sendmail(serstr, email):
    with tx.app_context():
        msg = Message(subject="老张大讲堂激活邮件", recipients=["2861358163@qq.com"])
        msg.html = "  <a href='http://127.0.0.1:19011/active/%s' >  点击激活用户%s  </a> " % (serstr, email)
        mail.send(msg)
