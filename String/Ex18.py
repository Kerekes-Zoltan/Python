"""
 Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt
"""
 
def first_three(string):
    #Return the first three chars of the given string
    return string[:3] if len(string) >= 3 else 5

#Sample usage
print(first_three('ipy'))   #Output: ipy
print(first_three('Python'))   #Output: Python
