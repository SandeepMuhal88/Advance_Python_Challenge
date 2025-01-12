# can we assign variable to empty class ?
# it is possible
# When python in program we can crete a class that both create dictionary
class Demo:
    pass

d1=Demo()
d1.a=10
d1.b=20
d1.name='Sandeep'
d1.Address='Karani Nagar'
print(d1.a)
print(d1.b)
print(d1.name)
print(d1.Address)
print(d1.__dict__)  # {'a': 10, 'b': 20, 'name': 'Sandeep', 'Address': 'Karani Nagar'}



# Comparison Between Class and Object
# Aspect	         :Class	                                                :Object
# Definition	     :A blueprint for creating objects.	                    :An instance of a class.
# Purpose	        :Defines attributes and methods.	                        :Represents a specific entity.
# Data Storage	    :Does not store data directly.	                        :Stores actual data and state.
# Example	         :Car (template for cars)	                                        :my_car (a specific car instance).