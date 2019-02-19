import threading
import time
import threading



# 定义一个全局变量 
g_num = 0


def test1(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print("----- in test1 g_num=%d --------" % g_num)


def test2(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----- in test2 g_num=%d --------" % g_num)


# 创建互斥锁
mutex = threading.Lock()


def main():

    t1 = threading.Thread(target = test1, args=(100000,))
    t2 = threading.Thread(target = test2, args=(100000,))


    t1.start()
    t2.start()


    time.sleep(5)
    print("----- in main g_num=%d --------" % g_num)



if __name__ == "__main__":
    main()
