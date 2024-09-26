"""
Write a Python program to create a histogram from a given list of integers.
"""

def create_histogram(values):
    for value in values:
        #Print the value followed by its histogram bar made of '*'
        print(f"{value}: " + "*" * value)
        
#List of integers (You can replace this with user input or any list)
values = list(map(int, input("Enter a list of integers (separated by space): ").split()))

#Create the histogram
create_histogram(values)