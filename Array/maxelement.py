from array import *
arr=[]
size=int(input("enter the size of array"))
for i in range(size):
    elements=int(input(f"Enter the {i+1} element "))
    arr.append(elements)
maximum=max(arr)
minimum=min(arr)

print(f"The array with the given size {size} is",arr)
print("The maximum element of array is:",maximum)
print("The minimum element of array is:",minimum)
