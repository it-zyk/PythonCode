



def main():
    file = open("README")
    text = file.read()
    file.close()
    print(text)
    
    print("-" * 50)

if __name__ == "__main__":
    main()
