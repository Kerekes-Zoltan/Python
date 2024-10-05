"""
Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""

def replace_not_poor(sentence):
    #Find the positions of 'not' and 'poor'
    not_position = sentence.find('not')
    poor_position = sentence.find('poor')
    
    #Check if 'not' appears before 'poor'abs
    if not_position != -1 and poor_position != -1 and not_position < poor_position:
        #Replace the substring form 'not' to 'poor' with 'good'
        sentence = sentence[:not_position] + 'good' + sentence[poor_position + 4:]

    return sentence

#Test cases
print(replace_not_poor('The lyrics is not that poor!'))
print(replace_not_poor('The lyrics is poor!'))