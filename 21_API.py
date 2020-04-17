import json
import urllib.request,urllib.parse,urllib.error
#This code will execute with API_KEY only, which i dont have, so the code is not executing.
serviceUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
     address = input('Enter address: ')
     if(len(address)<1):
         break

     url = serviceUrl + urllib.parse.urlencode({'Address' : address})
     print('Retreiving: ',url)
     url1 = urllib.request.urlopen(url)
     data = url1.read().decode()
     print('Retreived ',len(data),' characters.')

     try:
         list = json.loads(data)
     except:
         list = None

     if not list or 'status' not in list or list['status'] != 'OK':
         print('Error in data retrieval.')
         print(list)
         continue

     print(json.dumps(list, indent = 4))
     lat = list['results'][0]['geometry']['location']['lat']
     lng = list['results'][0]['geometry']['location']['lng']
     print('lat', lat, 'lng', lng)
     location = list['results'][0]['formatted_address']
     print(location)
