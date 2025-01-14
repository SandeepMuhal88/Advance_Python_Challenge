# Q20. explain Hierarchical Inheritance ?


# class ADD:
#     def Addition(self,a,b):
#         self.a=a
#         self.b=b
#         print(f"Addition= {self.a+self.b}")

# class SUB(ADD):
#     def Subtraction(self,a,b):
#         self.a=a
#         self.b=b
#         print(f"Subtraction= {self.a-self.b}")

# class MUL(ADD):
#     def Multiplication(self,a,b):
#         print(f"Multiplication= {a*b}")

# """That is provide multipy of two number"""
# obj=MUL()
# print(MUL.mro())
# obj.Addition(10,20)
# obj.Multiplication(10,10)
# ob1=SUB()
# ob1.Subtraction(20,10)


# Method Overriding

# class Parent:
#     def greet(self):
#         print("Hello from Parent!")

# class First_Child(Parent):
#     def greet(self):
#         print("Hello from FirstChild!")

# class Second_Child(Parent):
#     def greet(self):
#         print("Hello from SecondChild!")

# child1 = First_Child()
# child2 = Second_Child()

# child1.greet()
# child2.greet()


class Vehicle:
    def start(self):
        print("Starting the vehicle")

class Car(Vehicle):
    def start(self):
        print("Starting the car")
        super().start()

car = Car()
car.start()