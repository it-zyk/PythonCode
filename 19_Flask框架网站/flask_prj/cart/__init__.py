from flask import Blueprint

app_cart = Blueprint("app_cart", __name__, template_folder="templates")

# 在__init__.py文件被执行的时候，把视图加载进来，让蓝图与应用程序知道有视图的存在
