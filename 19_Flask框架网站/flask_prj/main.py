from flask import Flask
from goods import get_goods
from orders import app_orders
from cart import app_cart

# from goods import  get_goods
# from user import register
# 循环引用解决方法，推迟一方的导入，让一方先完成


app = Flask(__name__)

app.route("/get_goods")(get_goods)


app.register_blueprint(app_orders)
app.register_blueprint(app_orders, url_prefix="/orders")
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route("/")
def index():
    return "index page"


if __name__ == "__main__":
    print(app.url_map)
    app.run()
