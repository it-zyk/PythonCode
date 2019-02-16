




def main():
    try:
        num=int(input("请输入一个整数"))
    except ValueError:
        print("请输入正确的整数")
    except Exception as resutl:
        print("未知错误 %s" % result)

    print("-" * 50)



if __name__ == "__main__":
    main()
