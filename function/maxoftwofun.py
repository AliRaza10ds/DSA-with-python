num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

def maxoftwo(a,b):
    if a>b :
        return "The maximum number is:",a
    else:
        return "The maximum number is:",b
    
output=maxoftwo(num1,num2)
print(output)