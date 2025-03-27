"""
Write a Python program to remove a newline in Python.
"""

def remove_newline(input_string):
    
    #Removes newline characters from the input string
    return input_string.replace('\n', '')

#Example usage
if __name__ == '__main__':
    user_input = input("Enter a string with newlines (use Enter for newline): ")
    print("String after removing newlines:", remove_newline(user_input))