"""
Write a Python program to parse a string to float or integer.
"""

def parse_string_to_integer():
    
    #Get number from user
    value = input("Enter a number: ")
    try:
        #Try to convert string to integer
        data = int(value)
        print(f"The string was successfully parsed as an integer: {data}")
    except ValueError:
        try:
            #If integer parsing fails, try to convert to float
            data = float(value)
            print(f"The string was successfully parsed as float: {data}")
        except ValueError:
            #If both parsing attempts fail, report the error
            print(f"Error: '{value}' is not valid number.")
            
if __name__ == '__main__':
    parse_string_to_integer()