from array import *
arr=[]
nums_input=input("Enter the elements of array")
for i in nums_input:
    arr.append(i)
largest=arr[0]
print("The elements of the array is ",arr)

for element in arr:
    if largest <=element:
        largest=element
    else:
        largest=arr[0] 

print("The largest element in the given array is: ",largest)