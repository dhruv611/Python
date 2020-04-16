import json
input = '''
[
    {
        "Name" : "Dhruv",
        "ID" : "001",
        "atr" : "01"
    },
    {
        "Name" : "Sharma",
        "ID" : "002",
        "atr" : "02"
    }
]'''  #it is a list bcoz of [] and having 2 disctionaries inside it

try:
    list = json.loads(input)
except:
    print('Incorrect input provided.')
    quit()

print('Person Count: ',len(list),'\n')

for i in list:
    print('Name: ',i['Name'])
    print('ID: ',i['ID'])
    print('Attribute: ',i['atr'])
    print('\n')
