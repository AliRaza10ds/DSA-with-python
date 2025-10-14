def bmi_calculator(weight,height):
    bmi=round((weight/height**2),2)
    return bmi 


print("Welcome To BMI Calculator")
w=float(input("Enter your weight in kg"))
h=float(input("Enter your height in meters"))

result=bmi_calculator(w,h)
print("your BMI is",result)
if result <=18.5:
    print("You are Underweight")
elif 18.5 <result <=24.9:
    print("Your weight is normal")
elif 25 < result <= 29.29:
    print("You are overweight")
else:
    print("You are obese")

