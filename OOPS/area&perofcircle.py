import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area_of_circle(self):
        return math.pi *self.radius**2

    def perimeter_of_circle(self):
        return 2*math.pi *self.radius
radius=float(input("Enter the radius of circle"))
circle=Circle(radius)

area=circle.area_of_circle()
perimeter=circle.perimeter_of_circle()

print("The area of circle is:",area)
print("The perimeter of circle is:",perimeter)