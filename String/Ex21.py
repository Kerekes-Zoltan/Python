"""
Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
"""

def convert_if_2Upper_chars(string):
    
    #Convert the string to all uppercase if it contains at least two uppercase characters in the first 4 characters
    if sum(1 for c in string[:4] if c.isupper()) >= 2:
        return string.upper()
    return string

print(convert_if_2Upper_chars('PyThon'))    #Output: PYTHON
print(convert_if_2Upper_chars('java'))    #Output: java