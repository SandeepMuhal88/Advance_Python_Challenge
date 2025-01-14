class Bank:
    def __init__(self,ID,Name,Balance):
        self.ID=ID
        self.Name=Name
        self.Balance=Balance
    def diplsay(self):
        print("Bank Details")
        print(f"ID is {self.ID} , Name is {self.Name} and Balance is {self.Balance}")

class SBI(Bank):
    def __init__(self,Address,key1,key2,key3):
        self.key1=key1
        self.key2=key2
        self.key3=key3
        self.Address=Address
        super().__init__(self.key1,self.key2,self.key3)
    
    def diplsay(self):
        super().diplsay()
        print(f"Address is {self.Address}")
        print("I am from child class")

obj=SBI("Hyderabad",1041631,"Reserve Bank Of India",250000000)
obj.diplsay()