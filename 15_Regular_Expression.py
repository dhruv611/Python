##  ^	        Matches the beginning of a line
##  $	        Matches the end of the line
##  .	        Matches any character
##  \s	        Matches whitespace
##  \S	        Matches any non-whitespace character
##  *	        Repeats a character zero or more times
##  *?	        Repeats a character zero or more times (non-greedy)
##  +	        Repeats a character one or more times
##  +?	        Repeats a character one or more times (non-greedy)
##  [aeiou]	    Matches a single character in the listed set
##  [^XYZ]	    Matches a single character not in the listed set
##  [a-z0-9]	The set of characters can include a range
##  (	        Indicates where string extraction is to start
##  )	        Indicates where string extraction is to end

import re
handle = open('11_testfile.txt')
for i in handle:  #Example1
    i.split()
    if re.search('From:',i):  #this is similar to i.find('From:') > 0
        print('Text Found:',i)  # search() is for searching the data only and returns True/False only
    else:
        print('Not Found.')

for i in handle:  #Example2
    i.split()
    if re.search('^From:',i): #similar to i.startswith('From:') -  ^ is used for searching strings startingwith____
        print('New Text Found: ',i)

for i in handle:  #Example3
    i.split()
    if re.search('^F.*:',i):  #^-starting with F then . means any character and * means zero or more char before ':'
        print('Text Found: ',i)

for i in handle:  #Example4
    i.split()
    if re.search('^F\S+:',i):  #^-starting with F then \S means no whitespace and + means one or more char before space
        print('Text Found: ',i
