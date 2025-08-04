from array import *
arr=[]
size=int(input("Enter the size of array"))
for i in range(size):
    elements=int(input(f"enter the {i+1} element"))
    arr.append(elements)
total_sum=sum(arr)
print(f"The array of size {size} with elements {arr} is:",arr)
print("The total sum of all elements is :",total_sum)

