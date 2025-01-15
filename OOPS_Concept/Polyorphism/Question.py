# Q24. can a function inside a class have unlimited argument ?
# Ans: Yes

class Calculator:
    def add(self, *args):
        sum=0
        for i in args:
            sum+=i
        return f'Addition={sum}'
    

obj = Calculator()
print(obj.add(10, 20))
print(obj.add(10, 20, 30))
print(obj.add(10, 20, 30, 40))
print(obj.add(10, 20, 30, 40, 50))

# pyhon does not support method overloading
