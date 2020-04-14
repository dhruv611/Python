import xml.etree.ElementTree as ET  #importing the library to manupulate XML data
input = '''
<Company>
    <Employee>
        <Emp attr = "E1">
            <Name>Dhruv</Name>
            <EmpID attrEMPID = "ID_ATTR_01">001</EmpID>
            <DOJ>01-01-0001</DOJ>
        </Emp>
        <Emp attr = "E2">
            <Name>Great</Name>
            <EmpID attrEMPID = "ID_ATTR_02">002</EmpID>
            <DOJ>02-02-0002</DOJ>
        </Emp>
        <Emp attr = "E3">
            <Name>Greatest</Name>
            <EmpID attrEMPID = "ID_ATTR_03">003</EmpID>
            <DOJ>03-03-0003</DOJ>
        </Emp>
    </Employee>
</Company>'''

try:
    Company = ET.fromstring(input)  #to convert the XMl data into string
except:
    print('Incorrect XML provided.')
    quit()
list = Company.findall('Employee/Emp')   #to read all the xml data of tag EMP within Employee tag
print('Employee Count: ',len(list),'\n')

for i in list:
    print('Name: ',i.find('Name').text)   #to find the value in tag Name and .text is to print the value inside tag Name
    print('Employee ID:',i.find('EmpID').text)
    print('Employee ID attribute: ',i.find('EmpID').get('attrEMPID'))
    print('Date of joining: ',i.find('DOJ').text)
    print('Emp attribute: ',i.get('attr'))  #.get is to find the value in attribute
    print('\n')
