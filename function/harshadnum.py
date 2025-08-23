def is_harshad_number(number):
    sum_of_digit=0
    for digit in str(number):
        sum_of_digit=sum_of_digit + int(digit)

    if number % sum_of_digit ==0:
            print("The number is Harshad Number")
    else:
            print("The number is not a harshad number")
user_input=int(input("Enter the number"))
result=is_harshad_number(user_input)
print(result)
