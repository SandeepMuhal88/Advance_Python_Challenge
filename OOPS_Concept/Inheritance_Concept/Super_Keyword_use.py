class Student:
    def __init__(self,name,age,contact_number):
        self.name=name
        self.age=age
        self.contact_number=contact_number

    def display(self):
        print("***************************Student Details********************************")
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Contact Number={self.contact_number}")

class Teacher(Student):
    Name="Rahul"
    age=25
    contact_numbers=1234567890
    subject="Python"
    def display(self):
        super().display()
        print("***************************Teacher Details********************************")
        print(f"Name={self.Name}")
        print(f"Age={self.age}")
        print(f"Contact Number={self.contact_numbers}")
        print(f"Subject={self.subject}")

t1=Teacher("Sandeep",21,9876543210)
t1.display()