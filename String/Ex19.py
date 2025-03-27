"""Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python
"""

def last_part(string, char):
    
    #Return the part of the string before the specified character
    return string.split(char)[0] if char in string else string

#Sample
print(last_part('https://www.w3resource.com/python-exercises', '-'))    #Output:https://www.w3resource.com/python
