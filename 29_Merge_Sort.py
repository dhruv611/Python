def MergeSort(dataset):
    i=0
    j=0
    k=0
    if len(dataset) > 1:
        mid = int(len(dataset)/2)
        leftarray = dataset[:mid]
        rightarray = dataset[mid:]

        MergeSort(leftarray)   #to break the left array into signle element arrays
        MergeSort(rightarray)  #to break the right array into signle element arrays

        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                dataset[k] = leftarray[i]
                i +=1
            else:
                dataset[k] = rightarray[j]
                j +=1
            k +=1

        while i < len(leftarray):
            dataset[k] = leftarray[i]
            i +=1
            k +=1

        while j < len(rightarray):
            dataset[k] = rightarray[j]
            j +=1
            k +=1


list = [3,5,7,1,2,-1,34,-23,-34,0]
print(list)
MergeSort(list)
print(list)
