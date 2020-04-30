def main():
    x = {'A':1,'B':2,'C':3}
    func(x)

def func(kwargs):
    if len(kwargs):
        for k,v in kwargs.items():
            print(k,v)
            print(kwargs[k])  #using [k] for identifying which value needs to be printed for this key.

    else:
        print('Sorry')

if __name__ =='__main__': main()
