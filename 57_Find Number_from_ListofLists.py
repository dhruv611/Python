def findAll(lst,x):
    lst1 = list()
    for i in range(len(lst)):
        if lst[i] == x:
            lst1.append([i])
        elif isinstance(lst[i],list):
            for j in findAll(lst[i],x):
                lst1.append([i]+j)
    return lst1

def main():
    x = int(input('Enter a number to searched: '))
    lst = [1,[2,3,4],0,-1,[5,2,[1,2,3],3],[0,[-1,-2],[1,2]]]
    print(findAll(lst,x))

if __name__ == "__main__": main()
