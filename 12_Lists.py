a=[1,2,3]  #list of 3 integers
b=[4,[5,6],'Dhruv']  #List of int,sub-list and str
c=a+b   #to append the second list into first
print(c)
a.append('aksdh')  #append new entry at the end of list
print(a)
a.remove('aksdh')  #remove the last entry from the list
print(a)
d='Dhruv Sharma the great !'
e=d.split()  #by default it will split by 'space' else u can use any delimiter by mentioning as split(',')
print(e)

f=list() #list constructor - list f with no data
f.append('Dhruv') #adding data into list
f.append('Sharma')
print(f)
