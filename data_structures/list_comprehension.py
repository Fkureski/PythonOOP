#List Comprehension
    #Create a new list for a list that already exists


fruits1 = ['avocado', 'banana', 'strawberry', 'kiwi', 'pineapple']

'''fruits2 = []

for item in fruits1:
    if 'b' in item:
        fruits2.append(item)'''

fruits2 = [item for item in fruits1 if 'b' in item] 

print(fruits2)

#INTEGER

values = [x * 10 for x in range(6)]

'''for x in range(6):
    values.append(x * 10)'''

print(values)