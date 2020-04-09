import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating the socket
mysock.connect(('data.pr4e.org', 80)) # connecting with web server
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # encode() to convert data fron unicode to utf-8 for server use
mysock.send(cmd)

while True:
    data = mysock.recv(512)  # receinving the data using recv() where max length will be 512 chars
    if len(data) < 1:  # once no data means end of file
        break
    print(data.decode(),end='')  # print the data after decoding it

mysock.close()
