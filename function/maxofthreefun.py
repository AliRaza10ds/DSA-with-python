num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))


def max_three(a,b,c):
    if a>b & a>c:
        return "The maximum number is ",a
    elif b>a & b>c:
        return "The maximum number is ",b
    else:
        return "The maximum number is ",c
    

output=max_three(num1,num2,num3)
print(output)