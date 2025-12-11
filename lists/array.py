# Array (matriz)

from array import array

letters = ['a', 'b', 'c', 'd']
numbers_i = [10, 20, 30, 40]
numbers_f = [1.2, 2.2, 3.2]

print(letters)
print(numbers_i)
print(numbers_f)

letters = array('w', ['a', 'b', 'c', 'd'])
print(letters)
numbers_i = array( 'i', [10, 20, 30, 40])
print(numbers_i)
numbers_f = array( 'f', [1.2, 2.2, 3.2])
print(numbers_f)