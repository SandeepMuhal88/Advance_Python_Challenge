class Student:
    def __init__(self,name,age,hobby,Phone_number,address):
        super().__init__(Phone_number,address)
        self.name=name # Instance variable
        self.age=age # Instance variable
        self.hobby=hobby # Instance variable

    def stu_details(self):
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Hobby={self.hobby}")

class Person:
    def __init__(self,Phone_number,address):
        self.Phone_number=Phone_number # Instance variable
        self.address=address # Instance variable

    def per_details(self):
        print(f"Phone Number={self.Phone_number}")
        print(f"Address={self.address}")


class Officer(Student,Person):
    def __init__(self,name,age,hobby,Phone_number,address,officeID):
        self.officeID=officeID
        super().__init__(name,age,hobby,Phone_number,address)
    
    def off_details(self):
        print(f"Office ID={self.officeID}")

s1=Officer("Sandeep",21,"Coding","1234567890","Karani Nagar",1001)
s1.stu_details()
s1.per_details()
s1.off_details()


# class Student:
#     def __init__(self):
#         self.name="sandeep" # Instance variable
#         self.age=21 # Instance variable
#         print("I am calling from constructor class")
    
#     def display(self):
#         print(f"Name={self.name}")
#         print(f"Age={self.age}")

# class Person:
#     def __init__(self):
#         self.pname = "Soniya"  # Instance variable
#         self.page = 19# Instance variable

#     def display(self):
#         print(f"Name={self.pname}")
#         print(f"Age={self.page}")

# class Officer(Student,Person):
#     def __init__(self,officeID):
#         self.officeID=officeID
    
#     def display(self):
#         print(f"Office ID={self.officeID}")


# s1=Officer(1001)
# s1.display()
# s1.display