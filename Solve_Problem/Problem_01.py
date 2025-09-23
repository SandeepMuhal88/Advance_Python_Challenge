def Fizz_Buzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# n= int(input("Enter the number: "))
# Fizz_Buzz(n)

# Question_01

# def Fizz_Buzz(n):
# 	for i in range(1,n+1):
# 		if i%3 ==0 and i%5==0:
# 			return f"FizzBuzz"
# 		elif i%3==0:
# 			return f"Fizz"
# 		elif i%5==0:
# 			return f"Buzz"
# 		else: 
# 			return i


# n= int(input("Enter a number:- "))
# print(Fizz_Buzz(n))
# That is not working beacause the function is not return multiple 
