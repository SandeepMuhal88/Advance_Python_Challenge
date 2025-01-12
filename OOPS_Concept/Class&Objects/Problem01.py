# Q1. what is a class ?

# 1. variables (attributes)
# 2. methods (function)

# myth  => class consist of variable or methods (this will always not true)
# class is a blue print for creating object.

class Student:
    def info(self):
        """
        This method is used to print the student details
        """
        Name="Sandeep Muhal"
        Address="Karani Nagar"
        Age=21
        Grade='A'
        print(f"Name={Name}")
        print(f"Address={Address}")
        print(f"Age={Age}")
        print(f"Grade={Grade}")

    def Sum(self,a,b):
        """
        This method is used to calculate sum of two numbers
        """
        return a+b

# Seraching
class Solutation:
    def Claculate(self,l1,num):
        """
        This method is used to calculate the index of number
        """
        for i in range(len(l1)):
            if l1[i]==num:
                return i
            else:
                return -1
        

# Creating object
s1=Student()
s1.info()
s1.Sum(10,20)

s2=Solutation()
l1=[1,2,3,4,5]
print(s2.Claculate(l1,2))