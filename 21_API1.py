# Import required library
import requests
import json
#Enter the place name
place = input("Please enter place name: ")
#Place your google map API_KEY to a variable
apiKey = 'AIzaSyD_Rgn2W_FiJnLAPOGUb70R2qFIe2pXMBE'
#Store google geocoding api url in a variable
url = 'https://maps.googleapis.com/maps/api/geocode/json?'
# call get method of request module and store respose object
r = requests.get(url + 'address =' + place + '&key =' + apiKey)
#Get json format result from the above response object
res = r.json()
#print the value of res
print(res)
