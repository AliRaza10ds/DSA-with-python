input=int(input("Enter number to print the table"))

def table(number):
    for i in range(1,11):
        result= i*number
        print(number,"x",i,"=",result)

output=table(input)