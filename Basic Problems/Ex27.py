""" 
Write a Python program that concatenates all elements in a list into a string and returns it.
"""

def concatenates_element(values):
    #Convert each element to a string and concatenate them
    return ''.join(map(str, values))

#Example list of elements (You can replace this with user and input or any list)
values = input("Enter elements of the list separated by spaces: ").split()

#Concatenate the elements into a string
result = concatenates_element(values)
print("Concatenated string: ", result)