# Q28. how to create methods as (public, protected, private)?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def __ADD(self):
        print("This is private method")
    
    def _sub(self,x,y):
        return x-y
    def _mul(self,x,y):
        return x*y


obj = Person("Ravi", 30)
print(obj.get_age())
# obj._ADD()
print(obj._sub(10,5))
print(obj._mul(10,5))