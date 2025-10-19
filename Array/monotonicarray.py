from array import *
arr=[]
arra_elements=int(input("Enter the elements of the array"))
for i in arra_elements:
    arr.append(i)
print("The elements of the array are: ")

largest=arr[0]
smallest=arr[0]

for elements in arr:
    if largest >= elements and smallest <= elements:
        print("The given array is monotonic array ")
    else:
        print("The given array is not a monotonic array")