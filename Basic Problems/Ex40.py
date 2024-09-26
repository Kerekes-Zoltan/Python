"""
Write a  Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""

import math

def calculate_distance(x1, x2, y1, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

#Prompt user input
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))

distance = calculate_distance(x1, x2, y1, y2)
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")