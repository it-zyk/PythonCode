


def main():
    
    # 1.创建tcp 套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 本地信息绑定
    tcp_socket.bind("", 7878)

    # 接听模式
    tcp_socket.listen(128)

    # 等待客户端到来 返回元组
    client_socket,client_addr = tcp_socket.accept()

    # 接收对方发送过来的数据
    recv_data = client_socket.recv(1024)  # 接收1024个字节
    print("接收到的数据为:",recv_data.decode("utf-8")
            
    # 2.发送数据
    send_data = input("输入要发送的数据:")
    client_socket.send(send_data.encode("utf-8"))


    # 4.关闭套接字
    client_socket.close()
    tcp_socket.close()
    


if __name__ == "__main__":
    main()
