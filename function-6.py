import math

def CircleArea(r):
    area = math.pi * r**2
    return area

r = int(input("Enter the radius of a circle: "))
area = CircleArea(r)

print("The area of this circle is:", area)
