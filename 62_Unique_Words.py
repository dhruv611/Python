def countWords(file):
    d = dict()
    hand = open(file, encoding='utf=8')
    for i in hand:
        line = i.split()
        for j in line:
            j = j.lower()
            d[j] = d.get(j,0) + 1

    lst1 = list()
    for k,v in d.items():
        lst = (v,k)
        lst1.append(lst)

    lst1 = sorted(lst1,reverse=True)
    for k,v in lst1[:20]:
        print(v,k)



def main():
    file = input('Enter filename to be processed: ')
    countWords(file)

if __name__ == "__main__": main()
