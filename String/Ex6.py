"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

def add_suffix(word):
    if len(word) < 3:
        return word
    elif word.endswith('ing'):
        return word + 'ly'
    else:
        return word + 'ing'
    
#Test cases
print(add_suffix('abc'))
print(add_suffix('string'))
print(add_suffix('go'))