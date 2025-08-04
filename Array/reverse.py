size=int(input("Enter the size of array"))

arr=[]
for i in range(size):
    array_list=int(input(f"Enter element{i+1}:"))
    arr.append(array_list)

reversed_array=arr[::-1]
print("The original array is:",arr)
print("The reversed array is:",reversed_array)