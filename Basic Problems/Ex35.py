"""
Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
"""

def unique_result(a, b):
    
    #Check if the two integers are equal
    if a == b:
        return True
    
    #Check if the sum is equal to 5
    if a + b == 5:
        return True
    
    #Check if the difference is equal to 5
    if abs(a - b) == 5:
        return True
    
def main():
    #Prompt user for input
    try:
        number1 = int(input("Enter the first integer: "))
        number2 = int(input("Enter the second integer:"))
    
        result = unique_result(number1, number2)
        print(f"The result is {result}")
    
    except ValueError:
        print("Enter a valid integer")
    
if __name__ == '__main__':
    main()