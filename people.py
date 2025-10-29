class People:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def information(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Job: {self.job}\n')

    def promotion(self, new_job):
        print(f'{self.name} is promoted for {new_job}\n')

    def update_age(self, new_age):
        if new_age > self.age:
            print(f'Updating {self.name} age from {self.age} to {new_age}')
        else:
            print('To update age, it needs to be higher than the previous')

colaborator1 = People('Felipe', 25, 'Python Developer')
colaborator2 = People('Gabrielle', 22, 'Dentist')

colaborator1.information()
colaborator2.information()
colaborator1.promotion('Data Engineer')
colaborator2.update_age(23)