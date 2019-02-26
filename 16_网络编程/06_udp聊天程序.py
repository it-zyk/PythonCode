import socket

def udp_send_data(udp_socket):
    """发送消息"""
    dest_ip = input("请输入目标IP:")
    dest_port = int(input("请输入目标port"))
    send_data =input("请输入要发送的数据:")
    # 发送数据
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def udp_recv_data(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s,%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))
    


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   
    # 绑定本地端口
    udp_socket.bind(("", 7788))


    # 循环发送接受数据
    while True:

        print("-----聊天器------")
        print("1.发送消息")
        print("2.接收消息")
        print("0.退出系统")
        op = int(input("请输入选项"))
        if op == 1:
            # 发送数据
            udp_send_data(udp_socket)
        elif op == 2: 
            # 接受数据并显示
            udp_recv_data(udp_socket)
        elif op == 0:
            break
        else:
            print("无效的输入")


if __name__ == "__main__":
    main()


