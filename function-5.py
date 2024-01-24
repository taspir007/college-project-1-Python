import math

def calculate_triangle_area(a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return None  # Indicate that the triangle is not possible

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

area = calculate_triangle_area(a, b, c)

if area is not None:
    print("The area of this triangle is:", area)
else:
    print("Triangle is not possible.")
