from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    # 接受参数
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    # 参数判断
    if not all([user_name, password]):
        req = {
            "code": 1,
            "message": "invalid params"
        }
        return jsonify(req)
    if user_name == "admin" and password == "python":
        req = {
            "code": 0,
            "message": "login success"
        }
        return jsonify(req)
    else:
        req = {
            "code": 2,
            "message": "wrong user name or password"
        }
        return jsonify(req)


if __name__ == "__main__":
    app.run(debug=True)
