#14. What is a break, continue, and pass in Python? Explain with example?
# Break is Exit in loop and contineu os avoid a specific condition

for i in range(1,11):
    if i==8:
        continue
    print("Number:-",i)
print("")
for i in range(1,11):
    if i==5:
        break
    print("Number:-",i)