class Calculator:
    def __init__(self):
        self.class_name = self.__class__.__name__  
        
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiplication(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"


choice = {
    '1': 'addition',
    '2': 'subtraction',
    '3': 'multiplication',
    '4': 'division'
}

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

user_choice = input("Enter the operation number (1-4): ")


if user_choice in choice:
    user_input = float(input("Enter the first number: "))
    user_input2 = float(input("Enter the second number: "))
    
    
    calc = Calculator()
    

    if user_choice == '1':
        print(f"Addition result: {calc.add(user_input, user_input2)}")
    elif user_choice == '2':
        print(f"Subtraction result: {calc.subtract(user_input, user_input2)}")
    elif user_choice == '3':
        print(f"Multiplication result: {calc.multiplication(user_input, user_input2)}")
    elif user_choice == '4':
        print(f"Division result: {calc.division(user_input, user_input2)}")
else:
    print("Invalid operation entered. Please enter a valid operation number (1-4).")
