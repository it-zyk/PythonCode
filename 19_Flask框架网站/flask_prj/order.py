from flask import Blueprint


# 创建一个蓝图对象，蓝图就是一个小模块的抽象
app_orders = Blueprint("app_orders", __name__)


@app_orders.route("/get_orders")
def app_orders():
    return "get orders page"


@app_orders.route("/post_orders")
def post_orders():
    return "post orders page"
