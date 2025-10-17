# Calculate 0! to 5!

def factorial(n):
    fact=1
    # if n==0:
    #     return 1
    # else:
    #     return n*factorial(n-1)
    if (n<0):
        print("Not Defined")
    elif(n==0):
        print("That Factoriyal number is:-",n)
    else:
        while(n !=1):
            fact=fact*n
            n-=1
        print(fact)


factorial(5)