


class A:
    
    def test(self):
        print("test 方法")



    def demo(self):
        print("demo 方法")



class B:

    def test(self):
        print("test 方法")


    def demo(self):
        print("demo 方法")



class C(A,B):


    pass



if __name__ == "__main__":

    # 创建子类对象
    c = C()
    
    
    print(C.__mro__)
    
    # c.test()

    # 
    # c.demo()
