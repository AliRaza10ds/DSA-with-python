def reverse_string(sentence):
    result = sentence[::-1]  # Reversing the input string using slicing
    return result

user_input = input("Enter your string: ")
response = reverse_string(user_input)
print(response)