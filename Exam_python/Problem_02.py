#2. What are the types of loops in Python?
# For loop, While loop
# For loop is used to iterate over a sequence
# num=int(input("Enter a number: "))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# while loop is used to execute a block of statements repeatedly until a given condition is true
num=int(input("Enter a number: "))
i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i+=1
