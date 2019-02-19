

def loop_method():
    # 循环嵌套调用输出    
    row = 1

    while row <= 5:
        col = 0
        while col < row:
            print("*",end="")
            col += 1

        row += 1
        print("")



def new_method():
    row = 1
    while row <= 5:
        print("*" * row)
        row += 1


def main():
    new_method()
    
if __name__ == "__main__":
    main()
