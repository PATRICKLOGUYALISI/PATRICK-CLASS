class Shape:
    def __init__(self, type, sides,):
        self.type = type
        self.sides = sides
    
    def area(self):   
        print(f"{type}'s calculating Area with {self.sides} sides")
    
    

class Square(Shape):
    def __init__(self, type, sides, length):
        super().__init__(type, sides)
        self.length = length

    def area(self):
        print(f"Area = {self.length ** 2}")

square = Square("square", 4, 5)
square.area()




           