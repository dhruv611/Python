import sqlite3

con = sqlite3.connect('sqlite.db')  # This DB file was created from sqlite online version and saved in this folder then called here
cur = con.cursor()

cur.execute('''DROP TABLE EMP1''')

cur.execute('''CREATE TABLE EMP1 (EMP_ID INTEGER, NAME TEXT)''')
cur.execute('''INSERT INTO EMP1 VALUES(1,'DHRUV')''')
cur.execute('''INSERT INTO EMP1 VALUES(2,'DHRUV2')''')
cur.execute('''INSERT INTO EMP1 VALUES(3,'DHRUV3'),(4,'DHRUV4'),(5,'DHRUV5')''')  #INSERTING ,,ULTIPLE ROWS AT A TIME

con.commit()
ID = 5
for i in cur.execute('''SELECT EMP_ID,NAME FROM EMP1 WHERE EMP_ID = ?''',(ID,)):  #? TO PROVIDE DATA AFTER , I.E.(ID,) AND PREVENT SQL INJECTION
    print(i[0],i[1])        #i[0] is for EMP_ID and i[1] for NAME

for i in cur.execute('''SELECT EMP_ID FROM EMP'''):   #this shows we can use multiple tables from same DB
    print(i[0])

cur.close()
