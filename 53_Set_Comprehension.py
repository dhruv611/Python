def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    temp1 = [(t*9/5)+32 for t in ctemps]  #List comprehension
    print(temp1)

    temp2 = {(t*9/5)+32 for t in ctemps}  # Set comprehension and it will be giving unique value only as it is a set
    print(temp2)


    # build a set from an input source
    sTemp = "The quick brown fox jumped over the lazy dog"
    sUpper = {s.upper() for s in sTemp}  # Set comprehension with all uppercase but this eill be having blank space as well
    sUpper1 = {s.upper() for s in sTemp if not s.isspace()}  #removed space
    print(sUpper)
    print(sUpper1)


if __name__ == "__main__":
    main()
