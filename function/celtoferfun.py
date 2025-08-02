def celtofar(celsius):
    result = (celsius * 9/5) + 32
    return f"The {celsius}°C in Fahrenheit is {result}°F"

def fartocel(fahrenheit):
    result = (fahrenheit - 32) * 5/9
    return f"The {fahrenheit}°F in Celsius is {result}°C"

def main():

    print("For Celsius to Fahrenheit, press 1")
    print("For Fahrenheit to Celsius, press 2")
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        user_input = float(input("Enter temperature in Celsius: "))
        response = celtofar(user_input)
        print(response)
    elif user_choice == 2:
        user_input = float(input("Enter temperature in Fahrenheit: "))
        response = fartocel(user_input)
        print(response)
    else:
        print("Invalid choice! Please enter a valid choice.")


main()
