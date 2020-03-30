sum = 0
while True:
    try:
        inp = input('Enter a number: ')
        if inp == 'Done':
            break
        inp = float(inp)
        sum = sum + inp
    except:
        print('Not a number.')
        continue
print('Total: ',sum)
