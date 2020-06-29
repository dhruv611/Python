import pickle as p

def saveDict(dict1,path):
    with open(path,'wb') as file:
        p.dump(dict1,file)

def retrievDict(path):
    try:
        with open(path,'rb') as file:
            try:
                print('Data: ',p.load(file))
            except:
                print('No data found!')
    except:
        print('No such file exists.')

def main():
    dict1 = {'First Name': 'Dhruv',
             'Last Name': 'Sharma',
             'Age': 27,
             'Sex': 'Male'}
    path = input('Enter file path: ')
    req = input('Do you want to save the data or retriev the data(S/R): ')

    if req == 'S':
        saveDict(dict1,path)
    elif req == 'R':
        retrievDict(path)
    else:
        print('Incorrect response.')

if __name__ == "__main__": main()
