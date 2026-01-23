cars = ['X6','i5', 'i8']

client_choice = input('What is the car you want?')

if client_choice in cars:
        print('Available car')
else:
      print('Not available')

'''print('1 - X1\n2 - X6\n3 - i5\n4 - m2\n5 - i8')

client_choice = int(input('What is the car you want?'))
car = str

if client_choice == 1:
    car = 'X1'
elif client_choice == 2:
    car = 'X6'
elif client_choice == 3:
    car = 'i5'
elif client_choice == 4:
    car = 'm2'
elif client_choice == 5:
    car = 'i8'
else:
    print('Not a valid command!')

if car in cars:
    print('Available car')
else:
    print('Car is not availabe')'''