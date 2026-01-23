#Dictionarys
# Uses idex in Keys and Values format
# Accept all data types

'''studant = {'name': 'Ana', 'age': 16, 'score': 'A', 'approved': True}

studant.update({'name': 'Jose', 'score': 'B'})

studant.update({'adress': 'Street 1'})

del studant['age']

print(studant)

studant = {'name': 'Ana', 'age': 16, 'score': 'A', 'approved': True}

for keys, values in studant.items():
    print(keys, values)'''

studant = {
    'name': 'Ana', 
    'age': 16, 
    'score': 'A', 
    'approved': True, 
    'subjects': ['Fisics', 'Math','English'] }

print(studant)
print(studant.get('subjects'))
print(studant.items())
print(studant.keys())
print(studant.values())
print(studant.get('name'))