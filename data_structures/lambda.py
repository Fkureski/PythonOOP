# Lamba Function
# little function without name

def sum(x):
    result = lambda x: x + 10
    return result(x) * 4

#sum_ten = lambda x,y: x + y + 10

print(sum(2))