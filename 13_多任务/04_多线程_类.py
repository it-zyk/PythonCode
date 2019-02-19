

import threading
import time

class MyThread(threading.Thread):

    def run(self):

        for i in range(4):
            msg = "I'm " + self.name + '@'+ str(i)
            print(msg)
        



def main():
    
    t = MyThread()
    
    # 调用启动子线程
    t.start()

    
    print(threading.enumerate())

    time.sleep(1)

    print(threading.enumerate())


if __name__ == "__main__":
    main()
