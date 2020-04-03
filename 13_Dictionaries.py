a = dict()  #creating an empty dictionary
print(a)  #to print empty dict
a['1.'] = 'Dhruv'
a['2.'] = 'Sharma'
a['name:'] = 'No name'
a['Age:'] = 27
print(a)  #order of output may be not equal to the order of input
print(a['1.']) ## to print particular data
print(a.get('1.',-1)) #get() will return the value stored with key'1.' but if this key doesnt exist then default value -1
print(list(a)) #will print only the keys
print(a.keys())  #will print only the keys
print(a.values())  #will print only the values
print(a.items())  #will print key-values pairs

for b,c in a.items():  ## to print key-values not as a list;; b,c are key,value
    print(b,c)
