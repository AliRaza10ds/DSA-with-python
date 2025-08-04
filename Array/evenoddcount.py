arr=[]
size=int(input("Enter the size of array"))
for i in range(size):
    elements=int(input(f"Enter the {i+1} element of array "))
    arr.append(elements)

even_counts=0
odd_counts=0
for num in arr:
    if num%2==0:
        even_counts +=1
    else:
        odd_counts +=1

print(f"The array of given size {size} with the given elements is",arr)
print("The number of even numbers in the array is ",even_counts)
print("The number of odd numbers in the array is ",odd_counts)