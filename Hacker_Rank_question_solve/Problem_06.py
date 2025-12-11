# You are programming a self-service kiosk for a movie theater. 
# The theater has specific pricing rules based on the customer's age and whether they have a "Student ID".

age=int(input("Enter your age:-"))

if age<=12:
    print("Ticket price is $5.")
elif age>12 or age<=17:
    print("Ticket price is $10.")
elif age>17 or age<=64:
    print("Ticket price is $15")
else:
    print("Ticket price is $8")