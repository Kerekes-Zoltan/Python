"""
Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""

#Function to get distinct words and sort them
def sort_unique_words(input_string):
    #Split the input string into words using comma as a separator
    words = input_string.split(",")
    
    #Remove any leading or trailing whitespace from each word
    words = [word.strip() for word in words]
    
    #Convert the list to a set to remove duplicates, then sort it
    sorted_words = sorted(set(words))
    
    #Join the sorted words back into a comma-separated string
    result = ", ".join(sorted_words)
    
    return result

#Input from user
input_string = input("Enter a comma-separated sequence of words:")

#Get the distinct, sorted words
output = sort_unique_words(input_string)

#Print the result
print("Sorted unique words: ", output)