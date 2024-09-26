
"""Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum
"""

def sum_of_three(a, b, c):
    total_sum = a + b + c
    if a == b == c:
        return 3 * total_sum
    else:
        return total_sum
    
#Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = sum_of_three(num1, num2, num3)
print(f"The result is: {result}")