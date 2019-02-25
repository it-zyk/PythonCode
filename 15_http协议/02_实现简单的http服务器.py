import socket

def server_client(new_socket):
    """为这个客户端返回数据"""

    # 1.接受浏览器发送来的请求
    request = new_socket.recv(1024)
    print(request)

    # 返回http格式化的数据，给浏览器 
    # 准备发送给浏览器的数据
    response = "HTTP/1.1 200 OK \r\n"
    response += "\r\n"
    response += "<h1>Hello <h1>"
    new_socket.send(response.encode("utf-8"))
    
    #关闭套接字
    new_socket.close()

def main():
    """ 用来完成整体控制 """

    # 1 创建套接字
    tcp_serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # 2.绑定
    tcp_serve_socket.bind(("", 7890))
    
    # 3. 监听套接字
    tcp_serve_socket.listen(128)
    
    while True:
        # 4 等待客户的链接
        new_socket, client_addr = tcp_serve_socket.accept()


        # 5. 为这个客户端服务
        server_client(new_socket)
    
    # 4 关闭套接字
    tcp_serve_socket.close()



if __name__ ==  "__main__":
    main()
