user_input=int(input("Enter the radius of circle"))

def area_circle(radius):
    area=3.14*radius
    return area


answer=area_circle(user_input)
print("The area of circle with the radius {} is:{}" .format(user_input,answer))
