arr=[]
size=int(input("Enter the size of array"))
for i in range(size):
    elements=int(input(f"Enter the {i+1} element"))
    arr.append(elements)
positive_numbers=[]
for number in arr:
   if number>0:
     positive_numbers.append(number)

print("The positive number in the given array is:",positive_numbers)