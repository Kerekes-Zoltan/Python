"""
Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""

def sum_two_integers(number1, number2):

    #Sum two integers, returning 20 if the sum is between [15, 20]
    sum_numbers = number1 + number2
    if 15 < sum_numbers < 20:
        return 20
    return sum_numbers

def main():
    #Prompt user for input
    try:
        number1 = int(input("Enter the first integer: "))
        number2 = int(input("Enter the second integer: "))
        
        result = sum_two_integers(number1, number2)
        print(f"The result is {result}")
        
    except ValueError:
        print("Please enter valid integers.")
        
if __name__ == '__main__':
    main()