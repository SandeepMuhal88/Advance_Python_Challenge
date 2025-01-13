# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display(self):
#         print("Car Details")
#         print(f"Brand={self.brand}")
#         print(f"Model={self.model}")

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity

#     def display(self):
#         super().display()
#         print(f"Battery Capacity={self.battery_capacity}")


# car=ElectricCar("Tesla","Model S",'100 KWH')
# car.display()


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def BasicCalculator(self):
        print("Sum of two numbers",self.num1 + self.num2)
        print("Subtraction of two numbers",self.num1 - self.num2)
        print("Multiplication of two numbers",self.num1 * self.num2)
        print("Division of two numbers",self.num1 // self.num2)


class ScientificCalculator(Calculator):
    def __init__(self, num1, num2,l1,l2):
        super().__init__(num1, num2)
        self.l1=l1
        self.l2=l2

    def cube(self):
        return self.num1 ** 3
    def square(self):
        return self.num1 ** 2
    
    def List(self):
        print(self.l1)
        print(self.l2)
        print("Sum of two LIst",self.l1 + self.l2)

    def ScientificCalculator(self):
        super().BasicCalculator()
        print("Cube of a number",self.cube())
        print("Square of a number",self.square())

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
num=int(input("Enter size of list:"))
l1=[]
l2=[]
for i in range(num):
    l1.append(int(input(f"Enter first number for first list {i+1} index:")))
    l2.append(int(input(f"Enter second number for second list {i+1} index:")))

print("Basic Calculator")
obj=ScientificCalculator(x,y,l1,l2)
obj.ScientificCalculator()
obj.List()