# class Calculator:
#     def add(self, num1, num2, num3=0):
#         return f"Addition={num1 + num2+num3}"
#     def sub(self, num1, num2):
#         return f"Subtraction={num1 - num2}"


# obj = Calculator()
# print(obj.add(10, 20))
# print(obj.add(10, 20, 30))
# print(obj.sub(10, 20))


# Method -02
class Calculator:
    def add(self, num1, num2):
        return f"Addition={num1 + num2}"
    
    def add(self, num1, num2, num3):
        return f"Addition={num1 + num2+num3}"
    
    def sub(self, num1, num2):
        return f"Subtraction={num1 - num2}"
    
    def sub(self, num1, num2, num3):
        return f"Subtraction={num1 - num2-num3}"


obj = Calculator()
print(obj.add(10, 20))
print(obj.add(10, 20, 30))
print(obj.sub(10, 20))
print(obj.sub(10, 20, 30))

# concept 2
# python does not support method overloadin



