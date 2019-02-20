



def create_num(all_num):
    a, b = 0, 1
    current_num=0
    while current_num < all_num:
        ret = yield a 
        print(ret)
        a, b = b, a+b
        current_num += 1

    return "hello"


def main():
    obj =  create_num(10)
    ret = next(obj)
    print(ret)

    ret = obj.send("hello")
    print(ret)
 #
 #    for num in obj:
 #        print(num)



if __name__ == "__main__":
    main()
