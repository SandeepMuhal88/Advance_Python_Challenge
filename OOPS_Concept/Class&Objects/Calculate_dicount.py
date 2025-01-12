# Car Factory:

# Create a Car class with attributes brand, model, and price.
#Add a method to calculate the discounted price based on a percentage.
class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def calculate_discount(self,percentage):
        discount=self.price*(percentage/100)
        return self.price-discount
    def display_details(self):
        print(f"Brand={self.brand}")
        print(f"Model={self.model}")
        print(f"Price={self.price}")
    
c1=Car("Toyota","Innova",1000000)
print("----------------------------------------------------")
print("----------------------------------------------------")
c1.display_details()
print("Discount Price",c1.calculate_discount(60))