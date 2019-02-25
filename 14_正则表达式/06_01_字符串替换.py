import re



def main():
    # 替
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)

if __name__ == "__main__":
    main()
