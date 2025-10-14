num_input=int(input("Enter the number to find the factorial"))
factorial=1
if num_input <0:
    print("Factorial does not exist for n3gative number")
elif num_input==0:
    print("The factorial of zero is always 1")

else:
    for i in range(1,num_input+1):
        factorial=factorial*i
        print(f'The factorial of the given number{num_input} is {factorial}')