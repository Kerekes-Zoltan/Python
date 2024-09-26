"""
Write a Python program to get the volume of a sphere with radius six.
"""

import math

#Define radius user want to calculate
radius = float(input("Enter the radius: "))

#Calculate the volume
volume = (4/3) * math.pi * (radius ** 3)

#Print the volume
print(f"The volume of the sphere with radius {6} is {volume:.2f}")