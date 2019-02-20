 
class Fibonacci(object):

    def __init__(self, all_num):
        self.all_num = all_num 
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self


    def __next__(self):

        if self.current_num < self.all_num:

            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration






def main():
    fib = Fibonacci(20)
    for num in fib:
        print(num, end ="\t")
    print("")



if __name__ == "__main__":
    main()


