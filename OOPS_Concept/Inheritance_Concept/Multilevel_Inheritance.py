class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return f"Addition= ",self.a+self.b

class Subtraction(Addition):
    def __init__(self,a,b):
        super().__init__(a,b)
    def sub(self):
        return f"Subtraction= ",self.a-self.b

class Multiplication(Subtraction):
    def __init__(self,a,b):
        super().__init__(a,b)
    def mul(self):
        return f"Multiplication= ",self.a*self.b

class Division(Multiplication):
    def __init__(self,a,b):
        super().__init__(a,b)
    def div(self):
        return f"Division= ",self.a//self.b

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
obj=Division(x,y)
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())