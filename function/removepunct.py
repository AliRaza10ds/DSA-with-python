punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

input_string=input("Enter the String")
no_punc=''

for char in input_string:
    if char not in punctuations:
        no_punc=no_punc + char 
    


print("The string without the punctuation is as : ", no_punc)
