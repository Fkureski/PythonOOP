# Calculate the body mass bmi
# What is your hight in cm
# What is your weight in kg

# Less than 18,5 thin
# Between 18,5 and 24,9 normal
# Between 25 and 29,9 overwight
# Between 30 and 39,9 obesidy 
# More than 40 comorbidy

def bmi(height, weight):
    total = weight / (height/100)**2
    return total

hight = float(input('Enter your hight in cm:'))
weight = float(input('Enter your weight in kg:'))

your_bmi = bmi(hight, weight)

if your_bmi > 40:
    print(f'You have comorbidy')
elif your_bmi <= 40 and your_bmi >= 30:
    print(f'You have obesidy')
elif your_bmi <= 29.9 and your_bmi >= 25:
    print(f'You are overwight')
elif your_bmi <= 24.9 and your_bmi >= 18.5:
    print(f'You are normal')
else:
    print(f'You are thin')


