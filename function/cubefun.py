user_input=int(input("Enter the number to find the cube:"))

def cube(number):
    result=number**3
    return f"The cube of the number {number} is {result}"

response=cube(user_input)
print(response)