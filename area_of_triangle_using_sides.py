import math

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

p = 1/2 * (a + b +c)

area = math.sqrt(p * (p-a) * (p-b) * (p-c))

print(f"The area of the triangle is {area}")