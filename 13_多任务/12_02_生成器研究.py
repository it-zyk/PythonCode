



def create_num(all_num):
    print("------1------")
    a, b = 0, 1
    current_num=0
    while current_num < all_num:
        print("------2------")
        #print(a)
        yield a #如果一个函数中有yield语句，那么这个就不是函数，而是一个生成器的模板
        a, b = b, a+b
        current_num += 1
        print("------3------")

    return "hello"


def main():
    obj =  create_num(10)
    ret = next(obj)
    print(ret)
 #
 #    for num in obj:
 #        print(num)



if __name__ == "__main__":
    main()
