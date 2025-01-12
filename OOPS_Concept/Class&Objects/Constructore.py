class Student:
    def __init__(self,name,age,grade,address):
        self.name=name
        self.age=age
        self.grade=grade
        self.address=address

    def info(self):
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Grade={self.grade}")
        print(f"Address={self.address}")

s1=Student("Sandeep",21,"A","Karani Nagar")
s1.info()
print("----------------------------------------------------")
print("----------------------------------------------------")
print("Student Details")
print("First Student")
s2=Student("Rahul",26,"B","Pune")
s2.info()
print("Second Student")
s3=Student("Rajesh",27,"C","Nagpur")
s3.info()
print("Third Student")
s4=Student("Ramesh",28,"D","Nashik")
s4.info()
print("Fourth Student")
s5=Student("Shyam",29,"E","Aurangabad")
s5.info()