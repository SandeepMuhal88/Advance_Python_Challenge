# creating NUmpy array
import numpy as np

# Creating 1D array
print("Creating 1D array")
arr1=np.array([2,5,6,3,9,3,1,20,3,20,63])
print(arr1)

# Creating 2D array
print("Creating 2D array")
arr2=np.array([[2,5,6,3,9,3,1,20,3,20,63],[2,5,6,3,9,3,1,20,3,20,63]])
print(arr2)

# Creating 3D array
print("Creating 3D array")
arr3=np.array([[[2,5,6,3,9,3,1,20,3,20,63],[2,5,6,3,9,3,1,20,3,20,63],[2,5,6,3,9,3,1,20,3,20,63]]])
print(arr3)

# Creating 4D array
print("Creating 4D array")
arr4=np.array([[[[2,5,6,3,9,3,1,20,3,20,63],[2,5,6,3,9,3,1,20,3,20,63],[2,5,6,3,9,3,1,20,3,20,63]],[[2,5,6,3,9,3,1,20,3,20,63],[2,5,6,3,9,3,1,20,3,20,63],[2,5,6,3,9,3,1,20,3,20,63]]]])
print(arr4)

# user input a array
print("User input a array")
# num=int(input("Enter size of array:"))
# l2=[]
# l1=[]
# for i in range(num):
#     l1.append(int(input(f"Enter number for index {i+1}:")))
#     l2.append(int(input(f"Enter number for index {i+1}:")))
# arr5=np.array([l1,l2])
# print(arr5)

# useer input a 2d array
print("User input a 2D array")
row=int(input("Enter number of rows:"))
col=int(input("Enter number of columns:"))
l3=[]

for i in range(row):
    l1=[]
    for j in range(col):
        l1.append(int(input(f"Enter number of row{i+1} and coloumn{j+1}:")))
    l3.append(l1)

arr6=np.array(l3)

print(arr6)