class Car:
    def __init__(self,userBrand,userModel,userColor):
        self.Model=userModel
        self.Color=userColor
        self.Brand=userBrand
    def info(self):
        print("Car Details")
        print(f"Brand={self.Brand}")
        print(f"Model={self.Model}")
        print(f"Color={self.Color}")

c1=Car("Toyota","Innova","White")
c1.info()
print("----------------------------------------------------")
print("----------------------------------------------------")
c2=Car("TATA","Safari","Red")
c2.info()
print("----------------------------------------------------")
print("----------------------------------------------------")
c3=Car("Honda","City","Blue")
c3.info()