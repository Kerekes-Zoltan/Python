"""
Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
"""

#Define a function to return N copies of the first 2 characters
def copy_string(string_input, num):
    #Check if the length of the string is less than 2
    if len(string_input) < 2:
        return string_input * num   #Return N copies of the entire string
    else:
        return string_input[:2] * num #Return N of the first 2 characters
    
#Example usage
string_input = "P"
number = 5

#Call the function and print the result
result = copy_string(string_input, number)
print(result)