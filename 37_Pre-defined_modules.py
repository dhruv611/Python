import os
import random

def main():
    v = os.urandom(10).hex()  #generate random 10 byte number converted into hexadecimal
    print(v)
    v = os.name  ##get OS name
    print(v)
    v = os.getenv('PATH') ##get environmet and its path
    print(v)
    v = os.getcwd()  ##current working directory
    print(v)
    v = random.randint(1,100)  ##Generate random integer between 1 to 100
    print(v)
    v = list(range(10))
    print(v)
    random.shuffle(v)  ## to shuffle the items in a list
    print(v)

if __name__ == '__main__': main()
