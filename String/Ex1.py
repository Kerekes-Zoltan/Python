"""
Write a Python program to calculate the length of a string.
"""

#Function to calculate length of string
def string_length():
    #Get user input
    user_string = input("Please enter a string: ")
    
    #Calculate the length of the string
    length = len(user_string)
    
    #Display the result
    print(f"The length of the string is: {length}")
    
#Call the function
string_length()