#Multi and Multilevel Inheritance

#Grand Class
class Animal:
    def __init__(self, name):
        self.name = name

#Parent Class
class Predator(Animal):
    def hunt(self):
        print(f'The {self.name} is hunting!')

class Prey(Animal):
    def scaping(self):
        print(f'The {self.name} is running for life!')

#Child Class
class Rabbit(Prey):
    pass

class Tiger(Predator):
    pass

class Dolphin(Predator, Prey):
    pass

rabbit1 = Rabbit('Rabbit')
tiger1 = Tiger('Tiger')
dolphin1 = Dolphin('Dolphin')

rabbit1.scaping()
tiger1.hunt()
dolphin1.hunt()
