class Foo:
    def get_bar(self):
        return 'laowang'

    BAR = property(get_bar)




def main():
    obj = Foo()
    result = obj.BAR 
    print(result)


if __name__ == "__main__":
    main()
