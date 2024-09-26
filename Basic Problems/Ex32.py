"""
 Write a Python program to find the least common multiple (LCM) of two positive integers.
"""

import math

def gcd(a, b):
    """Compute the greatest common divisor using the Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the least common multiple."""
    return abs(a * b) // gcd(a, b)

def main():
    #Prompt user for input
    try:
        number1 = int(input("Enter the first positive integer: "))
        number2 = int(input("Enter the second positive integer: "))
        
        if number1 <= 0 or number2 <= 0:
            print("Both numbers must be positive integers.")
            return
        result = lcm(number1, number2)
        print(f"The least common multiple if {number1} and {number2} is {result}")
    
    except ValueError:
        print("Please enter vlaid integers.")
        
if __name__ == "__main__":
    main()