"""
Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
"""

def find_even_digit_numbers():
    even_digit_numbers = []
    
    #Iterate over the range of numbers from 100 to 400
    for num in range(100, 401):
        num_str = str(num)
        
        #Check if all digits in the number are even
        if all(int(digit) % 2 == 0 for digit in num_str):
            even_digit_numbers.append(num_str)
            
    #Join the numbers in a comma-sepparated sequence
    print(",".join(even_digit_numbers))
    
#Call the function
find_even_digit_numbers()