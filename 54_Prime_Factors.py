def isPrime(n):
    if n == 2:
        return 1
    elif n > 2:
        for i in range(2, n+1):
            if n == i:
                return 1
                break
            elif n % i == 0:
                return 0
                break
            i += 1

    else:
        return 0

def primeFactor(x):
    lst = list()
    y = 2
    while (x >= y):
        if isPrime(y):
            while (x%y == 0):
                x = x/y
                lst.append(y)
        y += 1;
    print(lst)

def main():
    x = int(input('Enter a number: '))
    primeFactor(x)


if __name__ == "__main__": main()
