from collections import Iterable
from collections import Iterator
import time



class Classmate(object):
    def __init__(self):
        self.name = list()
        self.current_num = 0

    def add(self, name):
        self.name.append(name)

    
    def __iter__(self):
        return self 
    
    
    def __next__(self):
        if self.current_num < len(self.name):
            ret = self.name[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration




def main():

    classmate = Classmate()

    classmate.add("老王")
    classmate.add("张三")
    classmate.add("李四")


    for name in classmate:
        print(name)
        time.sleep(1) 


if __name__ == "__main__":
    main()
