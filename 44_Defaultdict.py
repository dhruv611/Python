# Demonstrate the usage of defaultdict objects

from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = defaultdict(int)  #int is used to initialize every new key by an integer-----we can use lambda as well
#    fruitCounter = defaultdict(lambda: 100)       # by using lamda:100, all the count will start from 100

    # Count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1 #if fruitCounter is not a 'defaultdict' then we need to initialize every key for first time

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
