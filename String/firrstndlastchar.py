user_input=input("Enter the word")
if len(user_input)<2:
    print("Please enter the word greater than the lenght of two")
else:
    first_two=user_input[0:2]
    last_two=user_input[-2:]
    final_output=first_two + last_two
    print(final_output)