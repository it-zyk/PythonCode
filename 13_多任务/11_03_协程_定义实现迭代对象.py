from collections import Iterable
from collections import Iterator
import time



class Classmate(object):
    def __init__(self):
        self.name = list()


    def add(self, name):
        self.name.append(name)

    
    def __iter__(self):
        iterator = ClassIterator(self)
        return iterator 


class ClassIterator(object):
    
    def __init__(self, obj):
        self.current_num = 0
        self.obj = obj 

    def __iter__(self):
        pass


    def __next__(self):
        if self.current_num < len(self.obj.name):
            ret = self.obj.name[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration




def main():

    classmate = Classmate()

    classmate.add("老王")
    classmate.add("张三")
    classmate.add("李四")


    print("判断claassmate 是否可以迭代的对象:",isinstance(classmate, Iterable))

    classmate_iterator = iter(classmate)
    print("判断claassmate_iterator 是否是迭代器:",isinstance(classmate_iterator, ClassIterator))
    for name in classmate:
        print(name)
        time.sleep(1) 


if __name__ == "__main__":
    main()
