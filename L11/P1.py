#wapp to find area of circle and circumference of circle using math module


import math

r = float(input("enter the radius "))

a = math.pi * math.pow(r,2)
c = 2 * math.pi * r

print("area = ",round(a),"circumference = ",round(c))
