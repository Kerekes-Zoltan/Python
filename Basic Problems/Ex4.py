"""Write a Python program that calculates the area of a circle based on the radius entered by the user"""
import math
# Get the radius from the user
radius = float(input("Enter the radius you want to calculate: "))

# Calculate the area using the formula A = πr²
area = math.pi * (radius ** 2)

print(f"The area of the circle with radius {radius} is: {area:.2f}")