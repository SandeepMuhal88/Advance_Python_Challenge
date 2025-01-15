# Q30. find area of circle using abstraction ?
from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute 

    def get_area(self):  # Public method 
        return pi * (self.__radius ** 2)

    def set_radius(self, radius):  # Public method 
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("Radius must be positive")

num=int(input("Enter a Radius of circle:="))
circle = Circle(num)  
print("Area of the circle:", circle.get_area())