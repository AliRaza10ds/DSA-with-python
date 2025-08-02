import math
user_input=int(input("Enter the number to find the squareroot:"))

def sqrt(number):
    result=math.sqrt(number)
    return f"The squareroot of the number {number} is {result}"

response=sqrt(user_input)
print(response)
