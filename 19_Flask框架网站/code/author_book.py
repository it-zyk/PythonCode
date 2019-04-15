from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand



app = Flask(__name__)

class Config(object):
    '''sqlalchemy 的配置信息  '''
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/author_book_py04"


    # 设置sqlalchemy 自动跟踪数据库

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "DFGHJKLDFGHJKL"

app.config.from_object(Config)


db = SQLAlchemy(app)

# 1.创建Flask 脚本管理对象

manager = Manager(app)

# 2.创建数据库迁移工具对象

Migrate(app, db)

# 3 向manager 对象中添加数据库的操作命令

manager.add_command("db", MigrateCommand)


# 定义数据库的模型


class Author(db.Model):
    """作者 """
    __tablename__ = "tbl_authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")
    email = db.Column(db.String(64))
    mobile = db.Column(db.String(64))


class Book(db.Model):
    '''书籍 '''

    __tablename__ = "tbl_books"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer,db.ForeignKey("tbl_authors.id"))

# 创建表单类
class AuthorBook(FlaskForm):
    """作者书籍表单模型类"""
    author_name = StringField(label="作者", validators=[DataRequired("作者必填")])
    book_name = StringField(label="书籍", validators=[DataRequired("书籍必填")])
    submit = SubmitField(label="保存")




@app.route("/", methods=["GET", "POST"])
def index():
    form = AuthorBook()
    if form.validate_on_submit():
        # 验证表单成功

        # 提取表单数据库
        author_name = form.author_name.data
        book_name = form.book_name.data

        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name,author_id=author.id)
       # book = Book(name=book_name, author=author)
        db.session.add(book)
        db.session.commit()


    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li, form=form)



@app.route("/delete_book", methods=["POST"])
def delete_book():
    """"删除数据"""

    # 如果前端发送的请求t数据是json格式，get_json 会解析成字典

    req_dict = request.get_json(force=True)
    print(req_dict)
    book_id = req_dict.get("book_id");

    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    # return redirect(url_for("index"))
    # Content-type":"application/json"
    return jsonify(code=0, message="OK")


if __name__ == "__main__":
#    db.drop_all()
#    db.create_all()
#
#     #生成数据
#    au_xi = Author(name='我吃西红柿')
#    au_qian = Author(name='萧潜')
#    au_san = Author(name='唐家三少')
#
#    db.session.add_all([au_xi,au_qian,au_san])
#    db.session.commit()
#
#    bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
#    bk_xi2 = Book(name='寸芒', author_id=au_qian.id)
#    bk_qian = Book(name='飘渺之旅', author_id=au_san.id)
#    bk_san = Book(name='冰火魔厨', author_id=au_san.id)
#
#    db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
#    db.session.commit()
#
    #把数据提交给用户会话

    # 通过manager启动程
    manager.run()

    # app.run(debug=True)




