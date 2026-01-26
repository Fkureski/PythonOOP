'''def calc(num1):
    return num1**2

print(calc(2))

def sum(num1, num2):
    return num1 + num2

number1 = int(input('Type a number:'))
number2 = int(input('Type other number:'))
print(f'The sum of both is {sum(number1, number2)}')

def calc(base, exponent):
    return base**exponent

number1 = int(input('Type a number:'))
number2 = int(input('Type other number:') or 2)

print(f'The power is {calc(number1, number2)}')

def function(num):
    if num == 0 or num == 1:
        return 1
    return num * function(num - 1)

number = int(input('Type a number:'))
print(function(number))'''

def double(num):
#    result = num * 2
#    total = square(result)
    return num * 2

def square(num):
    return double(num) ** 2

number = int(input('Type a number:'))
print(f'The square of the double of {number} is {square(number)}')

