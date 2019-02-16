

class Dog(object):

    def __init__(self, name):
        
        self.name = name

    

    def game(self):

        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianQuan(Dog):

    
    
    def game(self):
        # 重写方法
        print("%s 飞到天上j去玩耍" % self.name)




class Person(object):
    

    def __init__(self, name):
        
        self.name = name


    def game_with_dog(self, dog):

        print("%s 和 %s 快乐地玩耍." % (self.name, dog.name))

        dog.game()




def main():
    # 1. 创建一个狗对象
    # wangcai = Dog("旺财")
    wangcai = XiaoTianQuan("飞天旺财")

    # 2. 创建一个小明对象
    xiaoming = Person('小明')


    # 3. 让小明调用狗玩 的方法

    xiaoming.game_with_dog(wangcai)

if __name__ == "__main__":
    main()

