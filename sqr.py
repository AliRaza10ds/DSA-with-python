import math
choice=int(input("Press 1 for square \n press 2 for squareroot"))
if choice==1:
    number=int(input("Enter the number to find the square"))
    result1=number * number
    print(result1)
elif choice==2:
    number2=int(input("Enter the number to find the squareroot"))
    result2=math.sqrt(number2)
    print(result2)
else:
    print("Invalid choice please enter a valid choice")
           