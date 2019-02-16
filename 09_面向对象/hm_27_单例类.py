

class MusicPlayer(object):
    
   
    instance = None

    
    def __new__(cls, *args, **kargs):
    
        # 1. 判断类属性是否为空对象
        
        if cls.instance is None: 
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        
        # 3. 返回类属性保存的对象引用

        return cls.instance
           






def main():
    player1 = MusicPlayer()
    print(player1)


    player2 = MusicPlayer()
    print(player2)





if __name__ == "__main__":
    main()
