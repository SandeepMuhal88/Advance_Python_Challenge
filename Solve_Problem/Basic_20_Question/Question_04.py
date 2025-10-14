# Print all the multiplication tables with numbers from 1 to 10


def print_table(n):
    for i in range(1,n+1):
        for j in range(1,11):
            print(i,"X",j,"=",i*j)
        print("Table of",i,"\n")

print_table(10)