"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

def within_100_of_1000_or_2000(num):
    return abs(1000-num) <= 100 or abs(2000-num) <= 100

#Test the function
number = int(input("Enter a number: "))
if within_100_of_1000_or_2000(number):
    print(f"The number {number} is within 100 of 1000 or 2000")
else:
    print(f"The number {number} is NOT within 100 of 1000 or 2000")