class revString(str):
    def __str__(self):
        return self[::-1]

def main():
    obj = revString('Dhruv Sharma.')
    print(obj)
    #following is an alternative for reversing a string
    a = 'sharma.dhruv1993@gamil.com'
    print(a[::-1])
    #following is for reversing a tuple
    b = (1,2,3,4,5)
    print(b)
    print(list(reversed(b)))

if __name__ == '__main__': main()
