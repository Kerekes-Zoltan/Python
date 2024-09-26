"""
Write a Python program to print without a newline or space.
"""

def print_without_newline_or_space():
    value = input("Enter string: ")
    
    #Print the value without space nor newline
    for i in value:
        #Use end="" to avoid newline and spaces
        print(i, end="")
        
    #Check for newlines
    print()

if __name__ == '__main__':
    print_without_newline_or_space()