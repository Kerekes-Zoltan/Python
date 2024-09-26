"""
Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference
"""

def difference_from_17(num):
    if num > 17:
        return 2*abs(num - 17)
    else:
        return 17 - num
    
#Test the function
number = int(input("Enter a number: "))
result = difference_from_17(number)
print(f"The result is: {result}")