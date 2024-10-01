"""
Write a Python program that checks whether a string represents an integer or not.
Expected Output:

Input a string: Python                                                  
The string is not an integer.  
"""

def check_integer(user_string):
    try:
        #Try converting the string to an integer
        int(user_string)
        print("The string is an integer.")
    except:
        #If conversion fails, it is not an integer
        print ("The string is not an integer.")
        
#Input from user
user_input = input ("Input a string: ")
check_integer(user_input)