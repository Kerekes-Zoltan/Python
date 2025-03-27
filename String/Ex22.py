"""
Write a Python program to sort a string lexicographically.
"""

def sort_string_lexicographically(input_string):
    
    #Convert the string to a list of characters
    c_string = list(input_string)
    
    #Sort the list of characters
    c_string.sort()
    
    #Join the sorted characters back into a string
    sorted_string = ''.join(c_string)
    return sorted_string

#Example usage
if __name__ == "__main__":
    user_input = input("Enter a string you want to sort: ")
    sorted_string = sort_string_lexicographically(user_input)
    print("Lexicographically sorted string:", sorted_string)