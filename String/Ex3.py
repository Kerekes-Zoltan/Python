"""
Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

def get_first_last_two_chars(input_string):
    # Check the length of the string
    if len(input_string) < 2:
        return ""  # Return empty string if less than 2 characters
    else:
        # Get the first 2 and last 2 characters
        first_two = input_string[:2]
        last_two = input_string[-2:]
        return first_two + last_two  # Concatenate and return

# Sample test cases
print(get_first_last_two_chars('w3resource'))  # Expected: 'w3ce'
print(get_first_last_two_chars('w3'))          # Expected: 'w3w3'
print(get_first_last_two_chars('w'))          # Expected: ''
