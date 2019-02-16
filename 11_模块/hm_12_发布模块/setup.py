from distutils.core import setup

setup(name="hm_message",  # 包名
        version="1.0",  # 版本
        description="发送和接收消息模块",  # 描述信息
        long_description="完整的发送和接收消息模块",  # 完整描述信息
        author="zyk",  # 作者
        author_email="it-zyk@outlook.com",  # 作者邮箱
        url="www.zyk.com",  # 主页
        py_modules=["hm_message.send_message","hm_message.receive_message"])

