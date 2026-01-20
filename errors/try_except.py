#Errors
    # Excelent to tests
    # Don't stop the program
    # Custom error messages

'''try:
    letters = ['a', 'b', 'c']
    print(letters[3])
except IndexError:
    print('Index do not exists')'''

try:
    value = int(input('Enter the product value:'))
    print(value)
except ValueError:
    print('Please enter a number')
finally:
    print('User submit the correct value')
    result = value + 2
    print(result)