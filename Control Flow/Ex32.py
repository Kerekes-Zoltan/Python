"""Write a Python program to check whether an alphabet is a vowel or consonant.
Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant."""


def check_character(user_input):
    # Define vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Check if the input is a single alphabet character
    if len(user_input) == 1 and user_input.isalpha():
        if user_input in vowels:
            print(f"{user_input} is a vowel.")
        else:
            print(f"{user_input} is a consonant.")
    else:
        print("Invalid input! Please enter a single letter of the alphabet.")
        
#Prompt user input
user_input = input("Input a letter of the alphabet: ")

#Call the function
check_character(user_input)