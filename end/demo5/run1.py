from gongchang import *
from models import *

if __name__ == '__main__':
    app = create_app()
    # db.drop_all()
    # db.create_all()
    # c = Category()
    # c.name = "武侠"
    # db.session.add(c)
    #
    # c1 = Category()
    # c1.name = "科幻"
    # db.session.add(c1)
    #
    # c2 = Category()
    # c2.name = "玄幻"
    # db.session.add(c2)
    # db.session.commit()
    # b = Book()
    # b.name="三体"
    # b.cid = 2
    # db.session.add(b)
    #
    # b1 = Book()
    # b1.name = "星球大战"
    # b1.cid = 2
    # db.session.add(b1)
    #
    # b2 = Book()
    # b2.name = "遮天"
    # b2.cid = 3
    # db.session.add(b2)
    #
    # b3 = Book()
    # b3.name = "悟空传"
    # b3.cid = 3
    # db.session.add(b3)
    # db.session.commit()

    app.run(host="127.0.0.1", port=19011, debug=True)
