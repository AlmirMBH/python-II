import time
# Loops

name = ''

while not name.strip():
    name = input('What is your name? ')

# print('Hi ' + str(name))

# start, end, step
for i in range(10, 20, 2):
    print(i+1)
    # 11, 13, 15, 17, 19

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(0)
print('Game over!')

rows = int(input('How many rows? '))
columns = int(input('How many columns? '))
symbol = input('What symbol? ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()

phone_number = '387-61-743-249'

for i in phone_number:
    if i == '-':
        continue
    else:
        if i == '3':
            pass
        else:
            print(i, end='')
