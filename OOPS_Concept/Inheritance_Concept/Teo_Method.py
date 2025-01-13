# Overriding Methods
# Same name method diffrent parameter
# A child class can override a method from the parent class, providing its own implementation.
# To invoke the parent class's method, use the super() function.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def info(self):
        print("Parent Class Method")
    

class Student(Person):
    def __init__(self,x,y):
        self.value1 = x
        self.value2 = y
        print("Sum of two numbers:",self.value1+self.value2)

    def display(self):
        print("Child Class Method")
    


obj=Person("Sandeep",21)
obj.display()
obj.info()
obj1=Student(10,20)
obj1.info()