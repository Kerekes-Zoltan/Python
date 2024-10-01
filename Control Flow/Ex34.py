"""
Write a Python program to sum two integers. However, if the sum is between 
15 and 20 it will return 20.
"""

def number_sum():
    #Prompt user to enter two values
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    
    sum = number1 + number2
    
    #Check if the sum is between 15 and 20
    if sum >= 15 and sum <= 20:
        sum = 20
    return sum

print("Sum of the two numbers is: ", number_sum())