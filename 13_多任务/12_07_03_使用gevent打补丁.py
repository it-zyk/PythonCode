import gevent
import time
from gevent import monkey

monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
