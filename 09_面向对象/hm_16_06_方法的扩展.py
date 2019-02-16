

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

    def bark(self):
        print("狗叫")



class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")


    def bark(self):

        # 1. 针对子类特有的属性编写代码
        print("叫得跟神一样.")


        # 2. 使用 super(), 调用原本父类中封装的方法
        super().bark()

        # 3. 增加子类的代码
        print("%$#%$##@@$%%#")



    class Cat(Animal):

        def catch(self):
            print("我会捉老鼠")



if __name__ == "__main__":

    

    xiao=XiaoTianQuan()
    
    #  子类扩展父类的方法
    
    xiao.bark()
    

    
