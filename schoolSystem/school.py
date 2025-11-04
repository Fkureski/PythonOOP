class School():
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status
    
    def presentation(self):
        print(f'My name is {self.name} and have {self.age} years old.')
        if not self.status:
            print('I`m curently out of School')
        print('I`m curently on School')

class Student(School):
    def __init__(self, name, age, year, status):
        super().__init__(name, age, status)
        self.year = year
    
    def presentation(self):
        super().presentation()
        print('And I`m a student \n')

class Teacher(School):
    def __init__(self, name, age, subject, status):
        super().__init__(name, age, status)
        self.subject = subject

    def presentation(self):
        super().presentation()
        print('And I`m a teacher \n')

class Assistent(School):
    def __init__(self, name, age, block, status):
        super().__init__(name, age, status)
        self.block = block
    def presentation(self):
        super().presentation()
        print('And I`m an assistent \n')

student1 = Student('Marcos', 14, 9, True)
teacher1 = Teacher('Andre', 34, 'Math', True)
assistent1 = Assistent('Mary', 29, 'Block B', False)

print(student1.name)
print(student1.age)
print(student1.year)

student1.presentation()
teacher1.presentation()
assistent1.presentation()