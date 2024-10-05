"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

def swap_strings(value1, value2):
    #Swap the first two characters of each string
    swapped_value1 = value2[:2] + value1[2:] #First two characters of value2 + rest of value1
    swapped_value2 = value1[:2] + value2[2:] # First two characters of value1 + rest of value2
    
    #Combine the swapped strings with a space in between
    result = swapped_value1 + ' ' + swapped_value2
    
    return result

#Sample test case
result = swap_strings('abc', 'xyz')
print(result)