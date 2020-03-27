inp = input('Enter your age in years: ')
try:
    inp = float(inp)
except:
    inp = -1
if inp == -1:
    print('Incorrect response.')
else:
    print('You have lived',inp*365,'days.')
print('Good Bye.')
