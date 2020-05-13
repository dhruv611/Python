def BubbleSort(dataset):
    for j in range(len(dataset)-1, 0, -1):  #range(len(dataset)-1, 0, -1) means start from no. of values-1 till 0 and decreament -1 every time
        for i in range(j): 
            if dataset[i] > dataset[i+1]:
                temp = dataset[i]
                dataset[i] = dataset[i+1]
                dataset[i+1] = temp
    print(dataset)


list = [3,5,7,1,2,-1,34,-23,-34,0]
print(list)
BubbleSort(list)
