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
num=int(input("Enter size of array:"))
l2=[]
l1=[]
for i in range(num):
    l1.append(int(input(f"Enter number for index {i+1}:")))
    l2.append(int(input(f"Enter number for index {i+1}:")))
arr5=np.array([l1,l2])
print(arr5)