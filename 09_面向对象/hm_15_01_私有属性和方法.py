

class Women:
    
    def __init__(self, name):

        self.name = name
        self.__age = 18


    
    def __secret(self):
        # 定义私有方法
        print("%s 的年龄是 %d" % (self.name, self.age))



xiaofang = Women("小芳")

# 私有属性不能被直接访问
# print(xiaofang.age)

xiaofang.secret()

