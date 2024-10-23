class Vehicle:
    def __init__(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    
    def __str__(self):
        return (f"this Vehicle is {self.color}")
        


#car1 = Vehicle("Red")
#print(car1)

class Car(Vehicle):
    def __init__(self,color, winter_tyres=False ):
        super().__init__(color)
        self.winter_tyres = winter_tyres
        
    def __str__(self):
        vehicle_str = super().__str__()
        return (f"{vehicle_str}\nHas Winter tyres: { self.winter_tyres}")
    
#car1 = Car("red",True)
#print(car1)


class Truck(Vehicle):
    def __init__(self, color, has_a_trailer = False):
        super().__init__(color)
        self.has_a_trailer=has_a_trailer
        
    def __str__(self):
        vehicle_str__ = super().__str__()
        return f"{vehicle_str__}\nhas trailer: {self.has_a_trailer}"
    
vehicle=Vehicle("blue")
car = Car("red",True)
truck = Truck("green", False)
    
print(vehicle)
print(car)
print(truck)

