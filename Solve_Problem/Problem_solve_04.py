# Problem 4: Sum of Digits
# Description:
# Write a function sum_of_digits(n) that takes a non-negative integer n and returns the sum of its individual digits.
# Examples:
# •	sum_of_digits(123) should return 6 (because 1+2+3=6).
# •	sum_of_digits(4589) should return 26 (because 4+5+8+9=26).



def sum_of_digits(n):
    n=str(n)
    x=0
    for i in n:
        x=x+int(i)
    return x
    


print(sum_of_digits(456))


# str=input("Enter a number: ")

# l1=list(str)
# print(l1)

# x=0

# for i in l1:
#     x=x+int(i)

# print(x)