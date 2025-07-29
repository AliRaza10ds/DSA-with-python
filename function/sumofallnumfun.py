input=int(input("enter the numbers"))


def sum(numbers):
    total=0
    for x in numbers:
        total +=x
        return total


output=sum(input)
print(output)