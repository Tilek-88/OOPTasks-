
class Airplane():
    def __init__(self,make,model,year,max_speed,odometer,is_flying):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying
        
    def get_take_off(self):
        self.is_flying = True
        print('vzlet')
    def get_fly(self):
        self.odometer += 10000
        print('letaet')    
    def get_land(self):
        self.is_flying = False
        print('prizemlenie')
    def get_Airplane(self):
        print(self.make,self.model,self.year,self.max_speed,self.odometer,self.is_flying)

Airplane1 = Airplane('Toyota','TU150','2005','240',10000, True)
Airplane1.get_Airplane()
Airplane1.get_take_off()
Airplane1.get_fly()
Airplane1.get_land()

