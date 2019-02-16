


class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


    @classmethod
    def show_tools_count(cls):

        print("工具对象的数量 %d " % cls.count)


    


def main():
    
    tool1 = Tool("榔头")
    tool2 = Tool("铁锹")

    Tool.show_tools_count()




if __name__ == "__main__":
    main()
