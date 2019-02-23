class Foo:
    def get_bar(self):
        return 'laowang'
    
    def set_bar(self, value):
        '''必须两个参数'''
        print("setter....")
        return 'set value' + value

    def del_bar(self):
        print("deleter....")
        return "laowang"

    BAR = property(get_bar, set_bar, del_bar, "description...")




def main():
    obj = Foo()
    result = obj.BAR
    desc = Foo.BAR.__doc__

    print(desc)


if __name__ == "__main__":
    main()
