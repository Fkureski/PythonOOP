# Filter Function

values = [10, 12, 34, 44, 57]

#def remove20(x):
#    return x > 20

#print(list(filter(remove20, values)))

print(list(filter(lambda x: x > 20, values)))