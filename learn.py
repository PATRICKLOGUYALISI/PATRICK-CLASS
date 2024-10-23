class Shape:
    def __init__(self, type, sides):
        self.type = type
        self.sides = sides
        print(f"{type}'s calculating Area {sides} sides")
    
    def area(self):
        pass  # To be defined in subclasses

class Square(Shape):
    def __init__(self, side_length):
        super().__init__('Square', 4)
        self.side_length = side_length

    def area(self):
        print(f"Area = {self.side_length ** 2}")

# Example usage
square = Square(5)
square.area()
