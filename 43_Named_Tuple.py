import collections

def main():
    Point = collections.namedtuple("Point","x y z")
    p1 = Point(1,2,3)
    p2 = Point(4,5,6)
    p3 = Point(7,8,9)

    print(p1)
    print(p2)
    print(p3)
    print(p1.z,p2.y,p3.x)

    p1 = p1._replace(x=5)
    print(p1)
    print(p1.x)


if __name__ == "__main__": main()
