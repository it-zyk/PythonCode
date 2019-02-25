import re



def main():
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")   
    # 切割字符串
    print(ret)



if __name__ == "__main__":
    main()
