"""
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5
"""


def print_numbers():
    #Loop through numbers from 0 to 6
    for i in range(7):
        #Skip the number 3 and 6
        if i == 3 or i == 6:
            continue
        #Print the numbers
        print(i, end=' ')

if __name__ == '__main__':
    print_numbers()