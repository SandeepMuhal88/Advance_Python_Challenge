# Q15. explain multiple inheritance ?

# Multiple inheritance is a feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes.
# It enables a child class to inherit and combine the functionality of multiple parent classes in a single class hierarchy.



# The reason the output is
# printed in brackets is that your methods (add, sub, and mul) return tuples instead of strings.
class Additaon:
    def add(self,a,b):
        return "Addition= ",a+b
    
class Subtraction:
    def sub(self,a,b):
        return "Subtraction= ",a-b
    
class Multiplication(Additaon,Subtraction):
    def mul(self,a,b):
        return "Multiplication= ",a*b

obj=Multiplication()
print(obj.add(10,20))
print(obj.sub(10,20))
print(obj.mul(10,20))

# that ouput is not in tuple form so we use f string
class Additaon:
    def add(self,a,b):
        return f"Addition= {a+b}"
    
class Subtraction:
    def sub(self,a,b):
        return f"Subtraction= {a-b}"
    
class Multiplication(Additaon,Subtraction):
    def mul(self,a,b):
        return f"Multiplication= {a*b}"

obj=Multiplication()
print(obj.add(10,20))
print(obj.sub(10,20))
print(obj.mul(10,20))