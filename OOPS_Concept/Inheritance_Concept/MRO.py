# class Parent1:
#     def greet(self):
#         print("Hello from Parent1!")

# class Parent2:
#     def greet(self):
#         print("Hello from Parent2!")

# class Child(Parent2, Parent1):
#     pass

# # Create an object of the child class
# child = Child()
# child.greet()

# print("Method Resolution Order (MRO):")
# print(Child.__mro__)
# # Output: Hello from Parent1!


# Q19.If class B overrides method of class A and class C inherits properties from class B .
# can we access method of class A from C's object.

class A:
    def greet(self):
        print("Hello from A!")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B!")
class C(B):
    pass

c = C()
c.greet()
