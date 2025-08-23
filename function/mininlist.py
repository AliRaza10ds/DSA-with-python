user_input=input("Enter the numbers")
def minimum(numbers):
    list_of_inputs=user_input.split()
    list_of_numbers=[int(x) for x in list_of_inputs]
    minimum= min (list_of_numbers)
    return f"The minimum element is {minimum}"

result=minimum(user_input)
print(result)