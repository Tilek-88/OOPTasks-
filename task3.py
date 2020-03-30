
class Car:
    def __init__(self, make, model, year, odometer, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70
    def drive(self, way):
        all_way = self.fuel*10
        if all_way<way:
            print("you need to refuel")
        else:
            self.__add_distance(way)
            self.subtract_fuel(way)
            print("Let's drive")
    
    def __add_distance(self, way):
        self.odometer += way
    
    def subtract_fuel(self, way):  
        self.fuel -= way/10

car1 = Car("Toyota", "Camry", 2005, 80, 120)
car1.drive()
car1.__add_distance()
car1.subtract_fuel()        