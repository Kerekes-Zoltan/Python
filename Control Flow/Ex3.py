"""
Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""
import random

#Generate a random number between 1 and 9
random_number = random.randint(1, 9)

#Main program loop
while True:
    
    #Prompt the user to guess a number
    user_number = int(input("Guess a number between 1 and 9: "))
    
    #Check if the guess is correct
    if user_number == random_number:
        print("Good Job!")
        break #Exist the loop if the guess is right
    else:
        print("Wrong guess, try again.")
        