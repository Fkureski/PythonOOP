#Do a program that can list the orders below:

# list 1 = Workers with car and work at night shift
# list 2 = Workers with car and work at day shift
# list 1 = Workers without car 

workers = ['Ana', 'Marcos', 'Alice', 'Peter', 'Sophia', 'Bruno', 'Melissa']
day_shift = ['Ana', 'Marcos', 'Alice', 'Melissa']
night_shift = ['Peter', 'Sophia', 'Bruno']
with_car = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#With list comprehension
print('List comprehension:')
list1 = [person for person in with_car if person in night_shift]
list2 = [person for person in with_car if person in day_shift]
list3 = [person for person in workers if person not in with_car]

print(f' List 1 = {list1} \n List 2 = {list2} \n List 3 = {list3}')

#With Sets
print('Sets:')

list1 = set(with_car).intersection(night_shift)
list2 = set(with_car).intersection(day_shift)
list3 = set(workers).difference(with_car)
print(f' List 1 = {list1} \n List 2 = {list2} \n List 3 = {list3}')


