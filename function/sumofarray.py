def sum_of_array(array):
    return sum(array)

user_input=(input("Enter the numbers to find the sum of all numbers"))
arr=list(map(int,user_input.split()))
result=sum_of_array(arr)
print(result)