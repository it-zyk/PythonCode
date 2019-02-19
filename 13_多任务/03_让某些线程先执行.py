import threading
import time



def dance():
    # 跳舞5秒钟
    for i in range(5):
        print("我正在跳舞")
    


def sing():
    # 唱歌5分钟
    for i in range(5):
        print("我正在唱菊花台")


def main():
    t1 = threading.Thread(target = dance)
    t2 = threading.Thread(target = sing)
    
    t1.start()
    
    time.sleep(1)

    t2.start()
   
    time.sleep(1)
    print(threading.enumerate())

if __name__ == "__main__":
    main()



