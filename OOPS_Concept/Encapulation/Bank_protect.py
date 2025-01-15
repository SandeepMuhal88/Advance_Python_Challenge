class Bank:
    def __init__(self,ID,Name,Balance,Pin):
        self._Account_Number=ID
        self.Name=Name
        self._Balance=Balance
        self.__Pin=Pin

    def deposit(self,amount):
        if amount>0:
            self._Balance=self._Balance+amount
            print(f"You have deposit {amount} and your balance is {self._Balance}")
        else:
            print("Invalid amount")
    
    def withdraw(self,amount):
        if amount>0 and amount<=self._Balance:
            self._Balance-=amount
            print(f"withdrawal amount is {amount} and your balance is {self._Balance}")
        else:
            print("Invalid amount")
    
    def set_pin(self,pin):
        self.__Pin=pin
    
    def get_details(self):
        print(f"Account Number is {self._Account_Number}")
        print(f"Name is {self.Name}")
        print(f"Balance is {self._Balance}")
    
    def get_balance(self):
        return self._Balance
    
    def get_pin(self):
        return self.__Pin

    
obj=Bank(123456789,"Sandeep",500000,1234)
obj.get_details()
obj.set_pin(461485)
obj.deposit(100000)
obj.get_details()