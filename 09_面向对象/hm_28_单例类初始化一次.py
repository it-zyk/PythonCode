

class MusicPlayer(object):
    
   
    instance = None

    # 记录是否执行过初始化动作
    init_flag = False    


    def __new__(cls, *args, **kargs):
    
        # 1. 判断类属性是否为空对象
        
        if cls.instance is None: 
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        
        # 3. 返回类属性保存的对象引用

        return cls.instance
           


    def __init__(self):
    
        # # 判断是否执行过初始化
        if MusicPlayer.init_flag:
            return
        # 2. 如果没有执行过 进行初始化
        print("初始化对象")
        
        # 3. 修改类属性的标记
        MusicPlayer.init_flag = True




def main():
    player1 = MusicPlayer()
    print(player1)


    player2 = MusicPlayer()
    print(player2)





if __name__ == "__main__":
    main()
