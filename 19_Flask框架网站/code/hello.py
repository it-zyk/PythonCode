
from flask import Flask



app = Flask(__name__,static_url_path="/python", # 访问静态资源的url前缀，默认值static
                      static_folder="static",   # 静态文件的目录，默认是static 
                      template_folder="templates" # 模板文件的目录，默认是templates:x
                      )



@app.route("/")
def index():
    return "hello flask"


if __name__ == "__main__":
    """启动Flask """
    app.run()

