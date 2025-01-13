class Student:
    def __init__(self,name,age,loaction,group):
        self.name=name
        self.age=age
        self.loacation=loaction
        self.group=group
        print("I am calling from constructor class")

    def info(self):
        Name="Rahul"
        Address="Karani Nagar,Bikaner"
        age=20
        print(f"Name:-{Name}\nAddress:{Address}\n Age:{age}")


obj=Student("Sandeep","2000","Ajmer rajsthan","Teja group")
obj1=Student("Rahul","500","Sikhar","Monster")

print(id(obj))
print(id(obj1))