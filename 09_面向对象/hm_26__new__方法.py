
class MusicPlayer(object):

    def __init__(self):
        print("初始化类对象")

    def __new__(cls, *args, **kargs):
        
        #  1.创建对象时， new 方法会自动调用
        print("创建对象，分配空间")


        # 2. 为对象分配空间

        instance=super().__new__(cls)
        
        return instance





def main():
    ms = MusicPlayer()
    print(ms)


if __name__ == "__main__":
    main()
