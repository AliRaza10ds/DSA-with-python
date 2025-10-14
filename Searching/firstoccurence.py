def occurence(arr,target):
    for char in arr:
        if char == target:
            return f"The first occurence of the element {target} is {arr[char]}"
        else:
            return "did not find the given element in the list"
        
user_input=input("Enter the elements")
user_input_tar=input("Enter the target element")
coded_input=list(map(int,user_input.split()))
coded_tar=list(map(int,user_input_tar.split()))
result=occurence(coded_input,coded_tar)
print(result)