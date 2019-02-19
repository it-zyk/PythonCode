




def main():
    
    # 1.打开文件
    file_read = open("README")
    file_write = open("READMENEW","w")


    # 2 读 写
    text = file_read.read()
    file_write.write(text)


    


    # 3.关闭
    file_read.close()
    file_write.close()



if __name__ == "__main__":
    main()
