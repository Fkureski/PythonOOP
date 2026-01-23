'''fruits = ['Apple', 'Strawberry', 'Grape']

for i in fruits:
    print(f'I like {i}')

for i in range(10):
    print(i + 1)

for i in range(1, 11, 1):
    print(i)

vegetables = ['Carrot', 'Lettece', 'Brocoli']

for i in vegetables:
    for t in fruits:
        print(f'Vegetable: {i} | Fruit {t}')

while num1 < 100:
    num1 += 1
    print(num1)

num1 = 0
num2 = 0

print('When num1 is 5 | break')
while num1 < 5:
    num1 += 1
    print(num1)
    if num1 == 5:
        break
for i in range(1, 11):
    if num1 == 5:
        break
    print(i)


print('While without 5 | continue')
while num2 < 10:
    num2 += 1
    if num2 == 5:
        continue
    print(num2)

for i in range(1, 11):
    if num1 == 5:
        continue
    print(i)'''

list1 = ['Apple','Apple','Apple','Grape','Banana','Strawberry']

count = 0
for fruit in list1:
    if fruit == 'Apple':
        count += 1

print(f'There are {count} apples')
