# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print('b :',b)

    s = "This is a string"
    print('s :',s)

    # Try combining them. This will cause an error:
    # print(s+b)

    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    s2 = b.decode('utf-8')
    print('s+b.decode(''urf-8'') :',s+s2)

    b2 = s.encode('utf-8')
    print('b+s.encode(''urf-8'') :',b+b2)

    # encode the string as UTF-32
    b3 = s.encode('utf-32')
    print('s.encode(''urf-32'') :',b3)
    print('s.encode(''urf-32'').decode(''utf-32'') :',b3.decode('utf-32'))

if __name__ == "__main__":
    main()
