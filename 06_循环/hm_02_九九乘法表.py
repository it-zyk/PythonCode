
def multiple_table():
     # 九九乘法表
    # * 后面是行号，*前面是列号
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %2d " %(col, row, col*row) , end=" ")
            col += 1
        print("")
        row += 1


def main():
    # 调用函数
    multiple_table()
   

if __name__ == "__main__":
    main()
