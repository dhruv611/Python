def test(c,d): #Function defined
    mul = c*d
    return mul
a = input('Enter first digit: ')
b = input('Enter second digit: ')
try:
    a = float(a)
    b = float(b)
except:
    print('Enter numbers only.')
    quit()   #Added this quit so that we dont encounter traceback when the compiles calls the test()
print('Multiplication Result : ',test(a,b))  #Function called/involked
