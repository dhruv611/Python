# Program to count 10 most common words
file = input('Enter file name: ')
handle = open(file)

dict = dict()
for i in handle:
    split = i.split()
    for j in split:
        dict[j] = dict.get(j,0)+1

list = list()
for k,v in dict.items():
    lst = (v,k)   #Converting the dictionary items into tuples means in key,value pairs in reverse order
    list.append(lst)  #adding the tuples in list

list = sorted(list,reverse=True)
# print(list[:10])
for k,v in list[:10]:
    print(v,k)
