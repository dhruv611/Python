a = 'Dhurv Sharma the great!'
b=0
for i in a:
    print(i)
    b=b+1

print('len(a):',len(a))
print(b)
print(a[1:5]) ##will from a[1] to a[4]
print(a[0:1])  ##will print a[0]
print(a[5:])   ##will print from a[5] to the end of string
print(a[:5])   ##will print till a[4] not a[5]
print(a[:])    ## will print whole string
