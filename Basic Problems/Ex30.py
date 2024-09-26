""" 
Write a Python program that will accept the base and height of a triangle and compute its area
"""

def triangle_area():
    #Enter the values to calculate the Area
    height = int(input("Enter the Height of the triangle: "))
    base = int(input("Enter the Base of the triangle:"))
    
    #Calculate the Area
    area = height * base / 2
    
    #Print the result
    print("Area for the triangle is: ", area)
    
triangle_area()