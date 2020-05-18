from datetime import datetime
from datetime import date
from datetime import time

obj = date.today()

print("Today's Date:",obj)
print("Date Components:",obj.day,obj.month,obj.year)
print("Weekday:",obj.weekday())
list = ["Mo","Tu","We","Th","Fr"]  #Mo is at position 0
print("today's Day:",list[obj.weekday()])

obj1 = datetime.now()

print("Date and Time:",obj1)
print("Only time:",obj1.time())

obj2 = datetime.now()

print(obj2.strftime("Current year: %Y"))
    # %a/%A - Weekday || %d/%D - Day/Date || %b/%B - Month || %y/%Y - Year
print(obj2.strftime("%A, %d %B %Y")) ##Lowercase will give abrriviated values and uppercase = complete values

    # %c - local date and time || %x - Local Date || %X - Local Time
print(obj2.strftime("%c,%x,%X"))

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print (obj2.strftime("Current time: %I:%M:%S %p")) # 12-Hour:Minute:Second:AM
print (obj2.strftime("24-hour time: %H:%M")) # 24-Hour:Minute
