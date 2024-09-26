"""Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument
"""

#Accept a function name from the user
function_name = input("Enter the name of a Python function: ")

#Display the documentation for the given function
help(function_name)

#Print the result
print(help)