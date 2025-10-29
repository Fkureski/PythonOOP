class Car:
    def __init__(self, colour, year):
        self.colour = colour
        self.year = year
        self.engineOn = True
        self.turnAlert = None

    def info(self):
        print(f'The car is {self.colour}')
        print(f'The fabrication year is {self.year}')

    def on(self):
        if not self.engineOn:
            self.engineOn = True
            print('The engine in on')
        else:
            print('The engine is already on')

    def off(self):
        if self.engineOn:
            self.engineOn = False
            print(f'The engine is off')
            return
        print(f'The engine is already off')

    def advertiseTurn (self, direction):
        if not self.engineOn:
            print('Power engine first')
            return
        
        self.turnAlert = direction
        print(f'Alert on for {direction}')

car1 = Car('Black', 2021)
car1.info()
car1.on()
car1.advertiseTurn('right')
car1.off()
