try:
    file = input('Enter filename to be opened: ')
    inp = open(file)
except:
    print('File cannot be opened.')
    quit()
for i in inp: #will print the data from file as it is
    print(i.rstrip())  #used rstrip() to remove extra new line char at the end of every line otherwise there will be 2 line gap(1. by print() and 2. from file itself)
# inp1 = inp.read() #will display complete file data in 1 line
# print(inp1)
