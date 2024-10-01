"""
Write a Python program to check the validity of passwords input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""

import re

def check_password_validity(password):
    
    #Check for minimum and maximum length
    if len(password) < 6 or len(password) > 16:
        return False
    
    #Regular expressions for different conditions
    if not re.search("[a-z]", password):  # At least 1 lowercase letter
        return False
    if not re.search("[A-Z]", password):  # At least 1 uppercase letter
        return False
    if not re.search("[0-9]", password):  # At least 1 digit
        return False
    if not re.search("[$#@]", password):  # At least 1 special character
        return False

    return True

#Taking input from user
password = input("Enter a password: ")

if check_password_validity(password):
    print("Password is valid!")
else:
    print("Password is invalid!")