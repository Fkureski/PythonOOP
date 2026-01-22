fruits = ['Banana', 'Apple', 'Orange', 'Pinapple']

print(fruits[0])
print(fruits[-1])

fruits[1:3] = ['Strawberry', 'Grape']
fruits.append('Watermelon')
print(fruits)

fruits.remove('Pinapple')
del fruits[-1]
print(fruits)