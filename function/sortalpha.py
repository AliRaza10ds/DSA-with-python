def sort_by_alphabet(string):
    words=[input.capitalize() for input in string.split()]
    words.sort()
    for word in words:
        print(word)

user_input=input("Enter the string")
sorted_string=sort_by_alphabet(user_input)
print(sorted_string)