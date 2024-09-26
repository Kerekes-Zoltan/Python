"""
Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
"""

def odd_or_ever(num):
    if num % 2 == 0:
        return "The number given is Even"
    else:
        return "The number given is ODD"
    
#Test the function
num = int(input("Enter a number: "))
print(odd_or_ever(num))