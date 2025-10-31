input_string=input("Enter the string")
default_string="ly"
default_string2="ing"

if len(input_string)<3:
    print(input_string)
else:
    if input_string[-3:]=="ing":
        print(input_string + default_string)
    elif input_string[-3:] !="ing":
        print(input_string + default_string2)
    else:
        print(input_string)

