class RBI:
    def RBI(self):
        print("I am from RBI method")

class SBI(RBI):
    def SBI(self):
        print("I am from SBI method")

class ICICI(RBI):
    def ICICI(self):
        print("I am from ICICI method")

class AXIS(SBI,ICICI):
    def AXIS(self):
        print("I am from AXIS method")

obj=AXIS()
print(AXIS.mro())
obj.RBI()
obj.AXIS()
obj.SBI()
obj.ICICI()


# Diamond Problem in Hybrid Inheritance
# The diamond problem arises when a class inherits from two classes that both 
# inherit from a common base class. This can lead to ambiguity in method resolution.
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent1(Grandparent):
    def greet(self):
        super().greet()
        
        print("Hello from Parent1")

class Parent2(Grandparent):
    def greet(self):
        super().greet()
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    def greet(self):
        super().greet()
        print("Hello from Child")

child = Child()
child.greet()

# Output: Hello from Parent1
