num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))
num3=float(input("Enter the third number"))
if num1>num2 and num1>num3:
    print(num1,"is the maximum")
elif num2>num1 and num2>num3:
    print (num2,"is the maximum")
else:
    print(num3,"is the maximum")