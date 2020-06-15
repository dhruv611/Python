# deque objects are like double-ended queues

import collections
import string


def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: " + str(len(d)))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # manipulate items from either end
    d.pop()   #pop from right
    d.popleft()  #pop from left
    d.append(2)
    d.appendleft(1)
    print(d)

    # rotate the deque
    print(d)
    d.rotate(5)  #rotate deque towards right by 5 elements
    print(d)


if __name__ == "__main__":
    main()