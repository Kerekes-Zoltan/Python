"""Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""

def multiple_strings(num, string_input):
    if num >= 0:
        return num * string_input
    else:
        return "N must be a non-negative integer"
    
#Test the function
number = int(input("Enter a non-negative integer:"))
string_input = input("Enter a string: ")

result = multiple_strings(number, string_input)
print(f"The result is: {result}")