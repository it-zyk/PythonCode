

class Animal:
    
    def eat(self):
        print("喝")


    def drink(self):
        print("喝")


    def run(self):
        print("跑")

    
    def run(self):
        print("睡")


class Dog(Animal):
    
    # 子类拥有父类中的所有方法 和 属性
#    def eat(self):
#        print("喝")
#
#
#    def drink(self):
#        print("喝")
#
#
#    def run(self):
#        print("跑")
#
#    
#    def run(self):
#        print("睡")
#

    def bark(self):
        print("叫")



class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")


if __name__ == "__main__":

    animal = Animal()
    
    animal.eat()
    animal.drink()
    animal.run()
    
    wangcai = Dog()

    wangcai.eat()
    wangcai.bark()

    xiao=XiaoTianQuan()
    xiao.fly()
    xiao.bark()
    xiao.eat()

