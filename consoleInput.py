# Input with validation
name = input('What is your name? ')
print('Hi ' + name)

age = int(input('How old are you? '))

if age < 30:
    print('Sorry ' + name + ', you are under 30, and you do not have access to this page.')
else:
    print('You are ' + str(age) + ' years old. Welcome to your page, ' + name + '.')

# Mathematical operations
print('Let\'s see what are the largest and smallest numbers, only integers allowed: ')
num1 = round(float(input('Enter 1st number: ')))
num2 = round(float(input('Enter 2nd number: ')))
num3 = round(float(input('Enter 3rd number: ')))

print(
      'The max number is ' +
      str(max(num1, num2, num3)) +
      ' and the smallest number is '
      + str(min(num1, num2, num3))
      )
