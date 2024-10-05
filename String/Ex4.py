"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

def replace_first_char(input_string):
    #Check if the string is empty
    if len(input_string) == 0:
        return input_string     #retrun the empty string if input is empty
    
    #Get the first character
    first_char = input_string[0]
    
    #Replace occurances of the first character (Except the first one)
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    
    return modified_string

#Sample test case
print(replace_first_char('restart'))