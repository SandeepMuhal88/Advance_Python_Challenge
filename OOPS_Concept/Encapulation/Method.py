# Access Modifier
# 1.Public
# 2.Private
# 3.Protected

class Person:
    def __init__(self,name,age,address,Gender,Phone_number):
        self.name=name
        self.age=age
        self._address=address
        self.__Phone_number=Phone_number
        self.__Gender=Gender
        
    def get_details(self):
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Address={self._address}")
        print(f"Phone Number={self.__Phone_number}")
        print(f"Gender={self.__Gender}")

    def set_details(self,name,age,address,Phone_number,Gender):
        self.name=name
        self.age=age
        self._address=address
        self.__Phone_number=Phone_number
        self.__Gender=Gender


obj=Person("Rahul",20,"Karani Nagar","Male",7878496344)
print(obj.name)
print(obj.age)
print(obj._address)
# print(obj.__Phone_number)
# print(obj.__Gender)  # AttributeError: 'Person' object has no attribute '__Gender'
obj.get_details()
obj.name="Soniya"
obj.age=21
obj._address="Choth ka Barwara"
obj.__Phone_number=1234567891
obj.__Gender="Female"   #Phone number and gender will not change
# Then we wand to change the phone number and gender then we use setter method
obj.set_details("Soniya",21,"Choth ka Barwara",1234567891,"Female")
obj.get_details()