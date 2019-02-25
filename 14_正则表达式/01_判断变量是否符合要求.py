import re



def main():
    names = ["age", "_age", "1age", "lage_1", "age!", 'a#123']
    
    for name in names:
        # ret = re.match(r"[a-zA_Z_][a-zA-Z0-9_]*",name)
        ret = re.match(r"[a-zA_Z_][a-zA-Z0-9_]*$",name)
        if ret:
            print("变量名：%s 符合要求...." % name)
        else:
            print("变量名：%s 不符合要求...." % name)

if __name__ == "__main__":
    main()
