import threading
import time




# 定义一个全局变量 
g_num = 100

gl_list = ["11", "22"]

def test1(tempt):
    global g_num
    g_num += 1
    tempt.append("34")
    print("----- in test1 g_num=%s --------" % str(tempt))


def test2(tempt):
    global g_num
    g_num += 1
    tempt.append("45")
    print("----- in test2 g_num=%s --------" % str(tempt))


def main():
    
    # target 指定将来在这个线程去哪里执行代码
    # args 指定将来调用函数的时候，传递什么数据过去

    t1 = threading.Thread(target = test1, args=(gl_list,))
    t2 = threading.Thread(target = test2, args=(gl_list,))

    
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)
    
    print("----- in main g_num=%s --------" % str(gl_list))
    


if __name__ == "__main__":
    main()
