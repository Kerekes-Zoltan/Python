"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

#Input data from user
input_data = input("Enter data: ")

#Convert input data string to list
data_list = input_data.split(',')

#Convert input data string to tuple
data_tuple = tuple(data_list)

#Print the results
print("List: ", data_list)
print("Tuple: ", data_tuple)