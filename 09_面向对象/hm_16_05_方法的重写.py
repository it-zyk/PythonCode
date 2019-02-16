

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


    def bark(self):
        print("叫得跟神一样.")

class Cat(Animal):

    def catch(self):
        print("我会捉老鼠")



if __name__ == "__main__":

    

    xiao=XiaoTianQuan()
    
    #  子类重写调用子类的方法，不会调用父类的方法 
    xiao.fly()
    xiao.bark()
    xiao.eat()

    
