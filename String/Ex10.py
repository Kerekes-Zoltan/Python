"""
Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
"""

def change_string_structure(string):
    if not string:  #Check if the string is empty
        return None
    #Returns the modified string
    return string[-1:] + string[1: - 1] + string[0]

#Example input
example_string = 'Zoltan'

#Output
print("Original string: ", example_string)
print("Modified string: ", change_string_structure(example_string))