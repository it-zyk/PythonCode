from . import app_cart


@app_cart("/get_cart")
def get_cart():
    return "get cart"
