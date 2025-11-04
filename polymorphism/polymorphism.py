# Polymorphism

class Personas():
    def talk(self):
        print(f'I`m a persona')

class Warrior(Personas):
    def talk(self):
        print(f'I`m a strong and furious warrior')

class Mage(Personas):
    def talk(self):
        print(f'I`m a wize and powerful mage')

class Archer(Personas):
    def talk(self):
        print(f'I`m a fast archer')


#Create objects

personas = [Warrior(), Mage(), Archer()]

for p in personas:
    p.talk()

#================================================================

class Dog:
    def sound(self):
        print('rof rof')

class Cat:
    def sound(self):
        print('meaw')

animals = [Dog(), Cat()]

for a in animals:
    a.sound()