def maximum(number):
    list_of_inputs=user_input.split()
    list_of_numbers=[int(x) for x in list_of_inputs]
    max_element=max(list_of_numbers)
    return f"The largest nunber in the given list is {max_element}"
user_input=input("Enter the numbers")
result=maximum(user_input)
print(result)