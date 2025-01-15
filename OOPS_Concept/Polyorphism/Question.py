# Q24. can a function inside a class have unlimited argument ?
# Ans: Yes

class Calculator:
    def add(self, *args):
        sum=0
        for i in args:
            sum+=i
        return sum
    

obj = Calculator()
print(obj.add(10, 20, 30, 40, 50))