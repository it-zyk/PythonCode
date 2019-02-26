import socket



def main():
    # 创建套接字 
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 对方的IP地址和端口号、
    dest_addr = ('10.2.34.31', 9001)
   
    # 必须绑定本机的IP和端口，绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)

    # 等待接受对方数据
    while True: 
        # 1024 本地最次接受最大地址
        recv_data = udp_socket.recvfrom(1024)     

        # 打印数据 recv_data 为元组(接受到的数据，(发送方的ip,端口号)
        recv_message = recv_data[0]  # 存储f接受到的数据
        recv_addr = recv_data[1]  # 存储发送方的地址信息

        #print("%s,%s" % (recv_data.decode("gbk"), str(send_addr)))

        print("%s,%s" % (recv_message.decode("utf-8"), str(recv_addr)))
    udp_socket.close()



if __name__ == "__main__":
    main()
