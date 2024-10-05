"""
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""

#Function to count character frequency in a string
def character_frequency(string):
    
    #Create an empty dictionary to store character frequency
    frequency = {}
    
    #Loop through each character in the string
    for char in string:
        #If the character is already in the dictionary, increment its count
        if char in frequency:
            frequency[char] += 1
        else:
            #If it's the first occurance, set the count to 1
            frequency[char] = 1
    return frequency

#Sample string
sample_string = 'google.com'
#Calculate character freqency
result = character_frequency(sample_string)

#Display result
print(f"Character Frequency: {result}")