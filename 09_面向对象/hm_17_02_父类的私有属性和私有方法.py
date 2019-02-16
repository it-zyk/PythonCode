


class A:
    
    def __init__(self):
        
        self.num1 = 100  
        self.__num2 = 200
        
    def __test(self):
        
        print("私有方法 %d %d" % (self.num1, self.__num2))


    def test(self):
        

        
        # 父类的公有的方法调用自己的私有属性
        print("父类的公有方法 %d", self.__num2)

        
        # 父类的公有的方法调用自己的私有方法
        self.__test()




class B(A):

    def demo(self):

        # 1 在子类中不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)


        # 2. 在子类中不能调用父类的私有方法
        # self.__test()
        
        # 3. 在子类中调用父类的公有方法 
        self.test()
        pass



if __name__ == '__main__':
    b = B()
    # print(b)
    
    # 调用父类的公有属性和方法
    print(b.num1)
    # b.test()
    b.demo()
    # 在外界不能访问对象的私有属性 和私有方法
    # print(b.__num2)


