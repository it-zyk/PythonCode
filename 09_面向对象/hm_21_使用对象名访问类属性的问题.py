


class Tool(object):
    
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    
    def __init__(self, name):
        self.name = name

        # 让类属性的值 +1
        Tool.count += 1

def main():
    tool1 = Tool("斧头")
    tool2 = Tool("榔头")
    tool3 = Tool("水桶")

    tool3.count = 99

    # 输出类属性值
    print("工具对象总数 %d",tool3.count)

    print("===> %d " % Tool.count)
if __name__ == "__main__":
    main()
