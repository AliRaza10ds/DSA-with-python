def len_string(string):
    result=len(string)
    return f"The lenght of the given string is", result 


user_input=input("Enter the string")
output=len_string(user_input)
print(output)