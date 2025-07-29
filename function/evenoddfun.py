user_input=int(input("Enter the number to check"))

def even_odd(number):
    if number <=0:
        return "Please enter a valid number"
    elif number % 2 ==0:
        return "The number is even"
    else:
        return "The number is odd"
    



answer=even_odd(user_input)
print(answer)
    