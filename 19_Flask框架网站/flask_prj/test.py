import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
    """"构建单元测试案例"""
    def setUp(self):
        # 创建进行Web 请求的客户端，使用flask框架提供
        self.client = app.test_client()

    def test_empty_user_name_password(self):
        """测试用户名密码不完整的情况"""
        # 创建进行web 请求的客户端，使用flask 提供的
        client = app.test_client()

        # 利用client 客户端模拟发送web请求
        resp = client.post("/login", data={})

        # ret 是视图返回的响应对象，data属性是响应体的数据
        resp = json.loads(resp)

        # 拿到返回值后进行断言调试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)


if __name__ == "__main__":
    unittest.main()
