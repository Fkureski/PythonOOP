class Engine:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
    
class Car:
    def __init__(self):
        self.engines = []
    
    def add_engine(self, engine):
        self.engines.append(engine)

    def listing_engines(self):
        for engine in self.engines:
            print(f'Brand: {engine.brand} // Power: {engine.power} cvs')


#Creating engines

v6_engine = Engine('Ford', 300)
v8_engine = Engine('Ferrari', 500)
v12_engine = Engine('Dodge', 800)

#Creating the car and adding its engine

car = Car()
car.add_engine(v6_engine)
car.add_engine(v8_engine)
car.add_engine(v12_engine)
car.listing_engines()
