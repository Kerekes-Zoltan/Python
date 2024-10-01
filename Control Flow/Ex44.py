"""
Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999
"""

def print_pattern(number):
    for i in range(1, number + 1):   #Loop from 1 to n
        for j in range(i):  #Loop i times
            print(i, end="")    #Print the number i without a newline
        print()     #Print a newline after each row
        
#Set the number of rows for the pattern
number_rows = 9
print_pattern(number_rows)