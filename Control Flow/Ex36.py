"""
Write a Python program to check if a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle
"""

def check_triangle(x, y, z):
    #Check if the three sides form a valid triangle
    if (x + y > z) and (x + z > y) and (y + z > x):
        #Check for equilateral triangle
        if x == y == z:
            print("Equilateral triangle")
        #Check for isosceles triangle
        elif x == y or y == z or z == x:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
            
    else:
        print("The sides do not form a valid triangle")
        
#Input the lengths of the sides of the triangle
x = int(input("Input length of side x: "))
y = int(input("Input length of side y: "))
z = int(input("Input length of side z: "))

#Call the function to check the triangle type
check_triangle(x, y, z)