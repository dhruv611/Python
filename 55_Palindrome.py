import re
def isPalindrome(x):
    y = str()
    badChars = ['0','1','2','3','4','5','6','7','8','9']
    for i in x:
        if i.isalnum():
            y += i
    x = str()
    for i in y:
        if i not in badChars:
            x = x + i.lower()
    y = x[::-1]
    print(x==y)

    ##OR we can use following
    x = "".join(re.findall(r'[a-z]+',x.lower()))
    y = x[::-1]
    print(x==y)

def main():
    x = input('Enter a string: ')
    isPalindrome(x)


if __name__ == "__main__": main()
