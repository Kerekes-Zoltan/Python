"""Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is
"""

def new_string_if_is(str):
    if str.startswith("Is"):
        return str
    else:
        return "Is" + str

#Test the function
input_string = input("Enter a string: ")
result = new_string_if_is(input_string)
print(f"The result is: {result}")