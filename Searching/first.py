def search_element(list,target):
    for char in list:
        if char== target:
            return target
        else:
            return -1
        
user_input=input("Enter the elements of the list")
target_element=input("Enter the target element")
coded_user_input=list(map(int,user_input.split()))
coded_target=list(map(int,target_element.split()))
result=search_element(coded_user_input,coded_target)
print(result)