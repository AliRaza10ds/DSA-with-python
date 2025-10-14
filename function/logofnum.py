import math
user_input=float(input("Enter the number "))
if user_input<=0:
    print("Please enter a valid number ")
else:
    result=math.log(user_input)
    print(result)