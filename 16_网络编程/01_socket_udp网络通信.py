import socket



def main():
    # 创建套接字 
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 对方的IP地址和端口号、
    dest_addr = ('10.2.34.31', 9001)
    
    send_data = input("请输入要发送的数据:")

    # 使用套接字发送数据
    udp_socket.sendto(send_data.encode("utf-8"), dest_addr)
    
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
