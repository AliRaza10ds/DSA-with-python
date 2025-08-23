def find_largest_element(arr):
    if arr==0:
        return "Array is empty"
    else:
        largest_element=0
        for element in arr:
            if element>largest_element:
                largest_element=element
        return largest_element
input_array=input("Enter the numbers of array")
mappeda_input=list(map(int,input_array.split()))
result=find_largest_element(mappeda_input)
print("The largest element in the array is : ",result)