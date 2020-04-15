import json

input = '''
{
    "Name" : "Dhruv",
    "ID" : {
        "type" : "Number",
        "Num" : "9599011195"
    },
    "email" : {
        "hide" : "Yes"
    }
}'''  #it is a disctionary bcoz having data in {}

try:
    list = json.loads(input)  #converting json data to list
except:
    print('Incorrect JSON data provided.')
    quit()

print('Name: ',list["Name"])  #single [] to print the value
print('ID: ',list["ID"])
print('Email: ',list["email"]["hide"])  #double [][] to print the attribute value
