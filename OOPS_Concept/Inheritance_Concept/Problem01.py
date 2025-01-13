# Q8. how many types of variables are there in python class ?

# there are two types of variables

# 1. instance variable = variable which inside a constructor are instance variables
# 2. class variable (static variable) = variable which outside of a constructor are class variables

# Instance variables are unique to each object

class Student:
    def __init__(self,name,age):
        self.name=name # Instance variable
        self.age=age # Instance variable

s1=Student("Sandeep",21)
s2=Student("Rahul",22)
s3=Student("Rajesh",23)
s4=Student("Ramesh",24)

print(s1.name,s1.age)
print(s2.name,s2.age)
print(s3.name,s3.age)
print(s4.name,s4.age)

# Static variable
class Person:
    species = "Human"  # Static variable (class variable)

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

# Access using class name
print(Person.species)  # Output: Human

# Access using an instance
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.species)  # Output: Human
print(person2.species)  # Output: Human

# Modifying the static variable affects all instances
Person.species = "Homo Sapiens"
print(person1.species)  # Output: Homo Sapiens
print(person2.species)  # Output: Homo Sapiens

