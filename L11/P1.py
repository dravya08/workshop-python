#wapp to find area & circumference of circle
# hint try to use math module

import math

radius = float(input("enter the radius "))
area = math.pi * math.pow(radius, 2)
cir = math.pi * 2 * radius

print("area = ", area)
print("************")
print("circumference", cir)