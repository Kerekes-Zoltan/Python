"""
Write a  Python program to test whether a passed letter is a vowel or not.
"""

#Define function to check if a letter is a vowel
def is_vowel(letter):
    #Define a set of vowels (both uppercase and lowercase)
    vowels = 'aeiouAEIOU'
    
    #Check if the pased letter is a single character and in the set of vowels
    if len(letter) == 1 and letter in vowels:
        return True
    else:
        return False
    
#Example usage
letter_input = input("Enter a letter: ")
    
#Call the function and print the result
if is_vowel(letter_input):
    print(f"The letter {letter_input} is a vowel.")
else:
    print(f"The letter {letter_input} is NOT a vowel.")