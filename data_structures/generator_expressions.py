#Generator Expressions

    #Faster lists, dictinarys, etc

from sys import getsizeof

numbers = [x * 10 for x in range(100000)]

print(type(numbers))
#print(numbers)
print(getsizeof(numbers))

print('-------------------------------------')

numbers = (x * 10 for x in range(100000))

print(type(numbers))
#print(numbers)
#print(list(numbers))
print(getsizeof(numbers))