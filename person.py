class Person:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
        
        
        
    def display_info(self):
        print(f"Name: {self.Name}, Age: {self.Age}")
        
class student(Person):
    def __init__(self, Name, Age, accessNumber):
        super().__init__(Name, Age)
        self.accessNumber = accessNumber
        
    def display_info(self):
        super().display_info()
        print(f"AccessNumber: {self.accessNumber}")
        
student1=student("PATRICK", 20, "B24341")
student1.display_info()
      
        
    
