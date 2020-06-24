def Sort(x):
    x = x.split()
    x = [i.lower()+ i for i in x]
    x.sort()
    x = [i[len(i)//2:] for i in x]
    x = ' '.join(x)
    print(x)


def main():
    x = input('Enter string: ')
    Sort(x)

if __name__ == "__main__": main()
