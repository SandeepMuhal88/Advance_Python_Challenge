class Person:
    address = "Karani Nagar"
    study = "B.Tech"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Address={self.address}")
        print(f"Study={self.study}")
    

class InheritsClass(Person):
    def add(self,a,b):
        return a+b
    def info(self):
        print("I from InheritsClass")
    
obj = InheritsClass("Sandeep", 21)
obj.display()
print("Sum of two numbers",obj.add(10,20))
obj.info()