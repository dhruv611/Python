import urllib.request,urllib.parse, urllib.error

handle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm') #will do all work of socket automatically
dict = dict()  #after importing the data, we can use it as we want
for i in handle:
    j = i.decode().split()
    for k in j:
        dict[k] = dict.get(k,0)+1

print(dict)
