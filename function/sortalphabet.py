def sort_alpha(string):
    words=[word.capitalize() for word in string.split()]
    words.sort()
    return words

input_string=input("Enter the words")
result=sort_alpha(input_string)
print(result)