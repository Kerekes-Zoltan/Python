"""
Write a Python program to count the number 4 in a given list.
"""

#Define a function to count the number of 4's in a list
def count_fours(num):
    return num.count(4)

#Example list
example_list = [1, 2, 3, 4, 4, 5, 5, 1, 4]

#Call the function and print the result
cnt = count_fours(example_list)
print(f"The result is: {cnt}")