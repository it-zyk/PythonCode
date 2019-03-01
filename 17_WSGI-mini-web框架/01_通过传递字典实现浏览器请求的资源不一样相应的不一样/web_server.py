import socket
import re
import multiprocessing
import time
import mini_frame


class WSGIServer(object):
    
    def __init__(self): 
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2.绑定
        self.tcp_server_socket.bind(("", 7890))
        
        # 3. 监听套接字
        self.tcp_server_socket.listen(128)

    def run_forever(self):
        while True:
            # 4 等待客户的链接
            new_socket, client_addr = self.tcp_server_socket.accept()
            
            # 创建线程
            p = multiprocessing.Process(target=self.server_client, args=(new_socket,))
            p.start()
            # 用mulltiprocessing创建进程时，子进程复制主进程资源
            new_socket.close()        
        
            # 5. 为这个客户端服务
            # server_client(new_socket)
        
        # 4 关闭套接字
        self.tcp_server_socket.close()


    def server_client(self, new_socket):
        """为这个客户端返回数据"""
        # 1.接受浏览器发送来的请求
        request = new_socket.recv(1024).decode("utf-8")
        # print("-" * 200)
        # print(request)
        
        request_line =request.splitlines()
        print("")
        print("-" * 20)
        print(request_line)

        ret = re.match(r"[^/]+(/[^ ]*)", request_line[0])
        # 返回http格式化的数据，给浏览器 
        # 准备发送给浏览器的数据
        
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
        
        if not file_name.endswith(".py"):

            # response += "<h1>Hello <h1>"
            try:
                f = open("./html" + file_name, "rb")
            except:
                response += "HTTP/1.1 404 NOT FOUND \r\n"
                response += "\r\n"
                response += "------------file not found-------"
                new_socket.send(response.encode("utf-8"));
            else:

                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK \r\n"
                response += "\r\n"
         
                new_socket.send(response.encode("utf-8"))
                # response body 发送给浏览器
                new_socket.send(html_content)
        else:
            
            env = dict()
            env["PATH_INFO"] = file_name 
            body = mini_frame.application(env, self.set_response_header)
            
            header = "HTTP/1.1 %s\r\n" % self.status 

            for tempt in self.headers:
                header += "%s:%s\r\n" % (tempt[0], tempt[1])
            header +="\r\n"


            response = header + body

            new_socket.send(response.encode("utf-8"))

    # respone header 发送给浏览器
    #关闭套接字
        new_socket.close()


    def set_response_header(self, status, headers):
        self.status = status
        self.headers =[("server","mini_web v8.0")]
        self.headers += headers 

             
def main():
    """ 用来完成整体控制 """
    msgi_server = WSGIServer()
    msgi_server.run_forever()




    # 1 创建套接字


if __name__ ==  "__main__":
    main()
