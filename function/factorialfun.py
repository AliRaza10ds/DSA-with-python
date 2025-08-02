import math
number=int(input("enter the number to compute th factorial"))

def factorial(user_input):
    result=math.factorial(user_input)
    return result



answer=factorial(number)
print(answer)


