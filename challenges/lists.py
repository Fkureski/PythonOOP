'''fruits = ['Banana', 'Apple', 'Orange', 'Pinapple']

print(fruits[0])
print(fruits[-1])

fruits[1:3] = ['Strawberry', 'Grape']
fruits.append('Watermelon')
print(fruits)

fruits.remove('Pinapple')
del fruits[-1]
print(fruits)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1,101))

for i in numbers:
    if i%2 == 0:
        print(f'{i} is par')
    else:
        print(f'{i} is odd')

cities = ('Curitiba','Rio','Sao Paulo')
user_city = input('Enter your city:')
if user_city in cities:
    print (True)
else:
    print(False)
print(cities)'''

countries_and_capitals = {
    'Brazil': 'Brasilia',
    'USA': 'Washington',
    'Greece': 'Athens',
    'Spain': 'Madrid',
    'England': 'London'
}
user_country = input('Enter your country:')
if user_country in countries_and_capitals.keys():
    print(f'The capital of {user_country} is {countries_and_capitals[user_country]}')
else:
    print('Not in our archive.')