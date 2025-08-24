def product_of_nums(input_list):
    numbers=[int(x) for x in input_list.split()]
    product=1
    for i in numbers:
        product = product*i
        print(product)
user_input=input("Enter the elements of list")
response=product_of_nums(user_input)
print(response)
