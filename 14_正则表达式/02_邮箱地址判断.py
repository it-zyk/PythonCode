import re
# 匹配y163邮箱地址，且@符合之前有4到20位英文字母下划线

def main():
    while True:
        intput_email = input("请输入您的邮箱地址:")
        # 如果正则表达式要用到某些普通字符如：. ? 仅仅需要在他们前面添加一个反斜杠进行转译#匹配前一个字符出现从m到n次
        email = re.match("^[a-zA-Z_0-9]{4,20}@163\.com$", intput_email)

        if email:
            print("你输入的邮箱地址：【%s】 符合要求" % intput_email)
            break
        else:
            print("您输入的邮箱地址【%s】不符合要求" % intput_email)
            


if __name__ == "__main__":
    main()
