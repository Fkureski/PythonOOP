class Animal:
    def __init__(self, name, colour, specie):
        self.name = name
        self.colour = colour
        self.specie = specie

    def presentation(self):
        print(f'This is a/an {self.specie} and its name is {self.name}')

class Cat(Animal):
    def sound(self):
        print('Meaw')
    
    def attack(self):
        print('The cat is scratching\n')

class Dog(Animal):
    def sound(self):
        print('Rof Rof')

    def attack(self):
        print('The dog is biting\n')

class Elephant(Animal):
    def sound(self):
        print('Pruuuuuuu...\n')


cat1 = Cat('Snow', 'White', 'Siamese Cat')
cat1.presentation()
cat1.sound()
cat1.attack()

dog1 = Dog('Calvin', 'Dark', 'Belgian Shepherd')
dog1.presentation()
dog1.sound()
dog1.attack()

elephant1 = Elephant('Fred', 'Brown', 'Asian Elephant')
elephant1.presentation()
elephant1.sound()