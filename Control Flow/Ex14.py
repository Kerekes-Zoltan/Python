"""Write a Python program that accepts a string and calculates the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2
"""

def number_of_letters_digits(input_string):
    letters = 0
    digits = 0
    
    #Iterate through each character in the string
    for char in input_string:
        if char.isdigit():      #Check if character is a digit
            digits += 1
        elif char.isalpha():    #Check if character is a letter
            letters += 1
    
    #Print result
    print(f"Letters: {letters}")
    print(f"Digits: {digits}")
    
#Sample input
input_string = input("Enter a string: ")
number_of_letters_digits(input_string)