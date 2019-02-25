import re



def main():

    
    # 切割字符串
    ret = re.split(r":| ","info:xiaoZhang 33 shandong")
    print(ret) 


if __name__ == "__main__":
    main()
