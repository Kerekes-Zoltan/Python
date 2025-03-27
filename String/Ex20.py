"""
Write a Python function to reverse a string if its length is a multiple of 4.
"""

def reverse_string_multiple_4(string):
    
    #Reverse the string if length is a multiple of 4
    return string[::-1] if len(string) % 4 == 0 else string

#Sample usage

print(reverse_string_multiple_4('abcd'))    #Output: dcba
print(reverse_string_multiple_4('python'))  #Output: python