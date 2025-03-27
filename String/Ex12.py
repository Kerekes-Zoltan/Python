"""
Write a Python program to count the occurrences of each word in a given sentence.
"""

#Function to count occurances of each word in a sentence
def count_word(sentence):
    #Convert the sentence to lowercase and split it into words
    words = sentence.lower().split()
    
    #Create an empty dictionary to store the word counts
    word_count = {}
    
    #Iterate through the words and count occurences
    for word in words:
        #If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        #Otherwise, add the word to the dictionary with a count of 1
        else:
            word_count[word] = 1
    
    return word_count

#Example usage
sentence = input("Enter a sentence: ")
word_occurrences = count_word(sentence)

#print the word counts
for word, count in word_occurrences.items():
    print(f"{word}: {count}")