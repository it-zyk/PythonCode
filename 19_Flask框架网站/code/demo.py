
from flask import Flask, render_template
from flast_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtfirns.validators import DataRequired
from time import time

app = Flask(__name__)



# 定义表单模型类
class RegisterForm(FlaskForm):
    '''自定义的注册表单模型类'''
    # 名字   验证器
    user_name = StringField(label="用户名",validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label="密码",validators=[DataRequired('')])
    


@app.route("/register")
def reqister():
    # 创建表单对象
    form = RegisterForm()
    return render_template("register.html",form=form)
















