"""
Write a Python program to check whether a string starts with specified characters.
"""

def check_Start(string, prefix):
    
    #Check if the string starts with the specified prefix
    if string.startswith(prefix):
        return True
    else:
        return False
    
#Example usage
string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

if check_Start(string, prefix):
    print(f"The string start with {prefix}")
else:
    print(f"The string does not start with {prefix}")