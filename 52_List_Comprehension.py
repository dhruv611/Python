def main():
    even = [2,4,6,8,10,12,14,16,18]
    mix = [1,2,3,4,5,6,7,8,9,10]

    evenSquare = list(map(lambda e: e**2, even)) ##normal way of doing this
    print(evenSquare)

    evenSquare = [e**2 for e in even]  ##List comprehension way
    print(evenSquare)

    mixEvenSquare = list(map(lambda e: e**2, filter(lambda e: e%2 == 0 ,mix)))## normal way of doing this
    print(mixEvenSquare)  # finding square of even digits from mix list

    mixEvenSquare = [e**2 for e in mix if e%2 == 0]  ##List comprehension way
    print(mixEvenSquare)


if __name__ == "__main__": main()
