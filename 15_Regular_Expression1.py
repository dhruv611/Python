import re
#findall() is used for extracting the data in regular expressions
handle = open('11_testfile.txt')
x = None

for i in handle:  #Example1
    i.split()
    x = re.findall('[A-Z0-9]+',i)  #[A-Z0-9] means any chars from A-Z or 0-9 without space and + meane >=1 or these before space
    print('Result: ',x)

for i in handle: #Example2
    i.split()
    x = re.findall('[AEIOU]+',i)  #[AEIOU] means any >=1 UPPERCASE VOWELS Before space
    print('Result: ',x)

for i in handle: #Example3
    i.split()
    x = re.findall('^F.+:',i)  #greedy matching - means it will fetch max line with last ':' (Ex: 'From: askjda:kjsdk:askdhksad' then it will fetch 'From: askjda:kjsdk:' instead of 'From:')
    print('Result: ',x)  # we can +? for non-greedy fetch

for i in handle: #Example4
    i.split()
    x = re.findall('\S+@\S+',i)  #will fetch all strings having @ in middle of non-space chars
    print('Result: ',x)

for i in handle: #Example5
    i.split()
    x = re.findall('^From: (\S+@\S+)',i)  # Extracts data that is between () - extract strings with @ in middle of non space chars from a line staring with 'From:'
    print('Result: ',x)

for i in handle: #Example6
    i.split()
    x = re.findall('@(\S+)',i)  # Extracts data that is between () - extract strings starting with @ till first space
    print('Result: ',x)

for i in handle: #Example7
    i.split()
    x = re.findall('\S+?@\S+',i)  # no greedy - extract strings starting having @ somewhere in middle, till first space
    print('Result: ',x)
