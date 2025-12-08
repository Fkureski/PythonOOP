#Functions with DRY  and XArgs

def sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(sum(2,3,4,7))


#Naming parameters

def car_store(**car):
    return car

print(car_store(brand='Audi', type='A3 Hatch', colour='Balck', engine=2.0, identification='ABC-1234'))


#4 * 3 * 2 * 1 = 24

import math

print(math.factorial(987456321))