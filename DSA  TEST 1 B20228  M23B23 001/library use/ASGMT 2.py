#2 Write a Python program to calculate the area of a parallelogram. The expected answer is 30.
import math

# Define the base and height of the parallelogram
area = [] # make a list
base = 5
height = 6

# Add the above to the list
area.append(base)
area.append(height)

print("Length of base: ",base)
print("Height of parallelogram: ",height)

# This will multiply base to height
print(math.prod(area))
