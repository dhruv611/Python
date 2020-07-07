import secrets as r  #secrets is used instead of random bcoz od security reasons

def password(length):
    list1 = ['Enter','number','of','words','Enter','number','of','words','Enter','number','of','words','Enter','1','2']
    lst = list()
    for i in range(length):
        lst.append(r.choice(list1))
    print(' '.join(lst))  ##printing password string from a predefinded list of elements

def main():
    length = int(input('Enter number of words: '))
    password(length)

if __name__ == "__main__": main()
