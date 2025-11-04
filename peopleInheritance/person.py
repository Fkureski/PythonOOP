class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def presentation(self):
        print(f'Hello, I`m {self.name} and I have {self.age} years old.')

class Colaborator(Person):
    def __init__ (self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def work(self):
        print(f'{self.name} is currently working as {self.job}\n')

class Client(Person):
    def __init__ (self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance

    def buy(self, price):
        if price <= self.balance:
            self.balance -= price
            print(f'Your purchase of {price} was approved. Your balance now is {self.balance}')
            return
        print('You don`t have enougth money to buy it')

    
colaborator1 = Colaborator('Felipe', 25, 'Python Jr developer')
colaborator1.presentation()
colaborator1.work()

client1 = Client('Gabrielle', 22, 200)
client1.presentation()
client1.buy(93)

