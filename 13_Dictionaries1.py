## Code to count the word with most occurences
file = input('Enter file name: ')
handle = open(file)

dict = dict()
for i in handle:
    splitFile = i.split()  #will spilt all the words in 1 line then will split next line on next iteration
    for j in splitFile:
        dict[j] = dict.get(j,0) + 1  #adding all the distinct keys and increasing their counts

print(dict) #printing the dictionary

Count = 0
Word = None
for word,count in dict.items(): # for finding the word with biggest occurence
    if Count < count:
        Count = count
        Word = word

print(Word,Count)
