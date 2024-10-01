"""
Write a Python program to find the median of three values.
Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0  
"""

def check_median(a, b, c):
    #Create a list of values
    values = [a, b, c]
    
    #Sort the list
    values.sort()
    
    #Print the middle value
    return values[1]

#Prompt user to insert values
a = float(input("Input first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

#Find and print the median
median = check_median(a, b, c)
print(f"THe median is {median}")