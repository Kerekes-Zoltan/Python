"""
Write a Python program to remove characters that have odd index values in a given string.
"""


def remove_odd_index(string):
    if not string:
        return None
    return string[::2]  #Slicing to keep characters at even indices

#Example usage
string = "Example"
result = remove_odd_index(string)

#Output
print("Original string: ", string)
print("String after removing odd index characters: ", result)