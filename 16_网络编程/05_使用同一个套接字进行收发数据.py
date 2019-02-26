import socket



def main():
    # 创建套接字 
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 获取对方的ip/port
    dest_ip = input("请输入对方的IP:")
    dest_port =int(input("请输入对方的port:"))

    # 对方的IP地址和端口号、
    dest_addr = (dest_ip, dest_port)

    send_data = input("请输入要发送的数据:")
    
    

    # 使用套接字发送数据
    udp_socket.sendto(send_data.encode("utf-8"), dest_addr)
    

    # 接收回来的数据
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
