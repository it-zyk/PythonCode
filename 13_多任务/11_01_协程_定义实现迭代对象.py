
from collections import Iterable
from collections import Iterator
import time



class Classmate(object):
    def __init__(self):
        self.name = list()


    def add(self, name):
        self.name.append(name)

    
    def __iter__(self):
        iterator = ClassIterator()
        return iterator 


class ClassIterator(object):
    
    def __iter__(self):
        pass


    def __next__(self):
        return "111"




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
