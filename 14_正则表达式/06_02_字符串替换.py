import re



def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


def main():
    # 替换
    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)

    ret = re.sub(r"\d+", add, "python = 99")
    print(ret)

 #
 #    python = 998
 #    python = 100
 #


if __name__ == "__main__":
    main()
