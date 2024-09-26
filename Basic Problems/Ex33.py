"""
Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""

def sum_three_integers():
    #Promtp the user to enter 3 numbers
    number1 = int(input("Enter the first integer: "))
    number2 = int(input("Enter the second integer: "))
    number3 = int(input("Enter the third integer: "))
    
    result = number1 + number2 + number3
    
    #Return the sum of three integers unless any two are equal, in which case return 0.
    if number1 == number2 or number1 == number3 or number2 == number3:
        return 0
    return result