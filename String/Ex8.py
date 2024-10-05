"""
Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""

def find_longers_word(words):
    if not words:   #Check if the list is empty
        return None, 0
    #Find the longest word based on length
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

#Sample list of words
words_list = ['Python', 'Kerekes', 'Learning']
longest_word, length = find_longers_word(words_list)

#Sample Output
print("Longest word: ", longest_word)
print("Length of the longest word: ", length)