"""
Write a  Python program that computes the greatest common divisor (GCD) of two positive integers.
"""

def gcd(a, b):
    #Ensure that A and B are positive values
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive integers.")
    
    #Implement Euclidean algoritm
    while b:
        a, b = b, a % b
    return a

#Example usage

if __name__ == "__main__":
    try:
        number1 = int(input("Enter the first positive integer: "))
        number2 = int(input("Enter the second positive integer: "))
        
        result = gcd (number1, number2)
        print(f"The GCD of number1:{number1} and number2: {number2} is {result}.")
        
    except ValueError as e:
        print(e)