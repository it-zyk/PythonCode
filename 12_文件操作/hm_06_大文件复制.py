




def main():
    
    # 1.打开文件
    file_read = open("README")
    file_write = open("READMENEW","w")

    while True:
        
        # 2 读 写
        text = file_read.readline()

        if not text:
            break

        file_write.write(text)

        # 读取指针和写入指针同时移动

    


    # 3.关闭
    file_read.close()
    file_write.close()



if __name__ == "__main__":
    main()
