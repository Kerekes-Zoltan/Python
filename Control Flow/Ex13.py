"""
Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
"""

def check_binary_divisible_by_5(binary_numbers):
    #Split the input string into individual binary numbers
    binary_list = binary_numbers.split(',')
    
    #Initialize an empty list to store binary numbers divisible by 5
    divisible_by_5 = []
    
    #Loop through each binary number
    for binary in binary_list:
        #Convert binary to decimal
        decimal_value = int(binary, 2)
        
        #Check if the decimal value is divisible by 5
        if decimal_value % 5 == 0:
            divisible_by_5.append(binary)
            
    return ','.join(divisible_by_5)

#Accept input from the user
binary_numbers = input("Enter comma-separated 4-digit binary numbers: ")

#Call kthe function and print the output
output = check_binary_divisible_by_5(binary_numbers)
print("Numbers divisible by 5: ", output)