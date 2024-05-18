import math

x1 = float(input("Enter the x-coordinate of the first vertex: "))
y1 = float(input("Enter the y-coordinate of the first vertex: "))

x2 = float(input("Enter the x-coordinate of the second vertex: "))
y2 = float(input("Enter the y-coordinate of the second vertex: "))

x3 = float(input("Enter the x-coordinate of the third vertex: "))
y3 = float(input("Enter the y-coordinate of the third vertex: "))

a = math.sqrt((x1-x2)**2 + (y1-y2)**2) # distance between the 1st and 2nd vertices
b = math.sqrt((x2-x3)**2 + (y2-y3)**2)
c = math.sqrt((x3-x1)**2 + (y3-y1)**2)


p = 1/2 * (a + b + c)

area = math.sqrt(p * (p-a) * (p-b) * (p-c))

print(f"The area of the triangle is {area}")