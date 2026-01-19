#Sets don't have indexes.
# Set avoid duplicated items


'''list1 = [10, 20, 30, 40, 50]
list2 = [10,20,60,70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # UNION

print(num1 - num2) #Difference
print(num2 - num1)

print(num1 ^ num2) #Symetric Difference

print(num1 & num2) #and

print(len(num1))


s1 = {1, 2, 3, 4, 5, 5}
s1.update([6, 7, 8, 9, 10])
s1.remove(1)
s1.discard(90)

print(list1)
print(s1)
print(type(list1))
print(type(s1))'''

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.symmetric_difference(set2)

print(set4)