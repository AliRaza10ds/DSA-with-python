import math
number=float(input("Enter the number to find the log"))
if number <=0:
    print("Please enter a valid number")
else:
    result=math.log(number)
    print("The log of the entered number is ",result)