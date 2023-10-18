#2 Write a Python program to calculate the area of a parallelogram. Expected answer is 30.0
import math

area = []
base = 5
height = 6

area.append(base)
area.append(height)

print("Length of base: ",base)
print("Height of parallelogram: ",height)
print(math.prod(area))
