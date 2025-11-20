from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def parameter(self):
        return 2 * 3.14 * self.radius

class ColoredShape(Shape):
    def __init__(self, color):
        self.color = color
    
    def area(self):
        return "Colored Shape"
    
    def parameter(self):
        return "Colored Shape"
    
    def get_color(self):
        return self.color

obj1=Circle(5)
obj2=ColoredShape("Red")
print(obj1.area())
print(obj1.parameter())
print(obj2.get_color())
print("Area:", obj1.area())
print("Parameter:", obj1.parameter())