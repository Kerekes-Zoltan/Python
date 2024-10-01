"""
 Write a Python program that accepts a word from the user and reverses it.
"""

#Promt user to insert word
word = input("Enter a word: ")

#Reverse the word using slicing
reversed_word = word[::-1]

#Display the reversed word
print("Reversed word: ", reversed_word)