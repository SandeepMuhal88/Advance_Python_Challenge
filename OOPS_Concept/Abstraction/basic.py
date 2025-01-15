from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def show(self):
        pass

    def display(self):
        print("Display Method")
    
    def get_details(self):
        pass

class B(A):
    def show(self):
        print("Show Method")

    def get_details(self):
        self.name="Rahul"
        self.age=20
        self.address="Karani Nagar" 
        self.phone_number=123456789
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Address={self.address}")
        print(f"Phone Number={self.phone_number}")
        print("Get Details Method")

obj = B()
obj.show()
obj.get_details()
obj.display()