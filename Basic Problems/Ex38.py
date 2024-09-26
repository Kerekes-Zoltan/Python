"""
Write a  Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""
#Function to calculate (x + y) * (x + y)
def function():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    
    #
    result = (number1 + number2) ** 2
    print(f"({number1} + {number2}) ^ 2 = {result}")

#Call function to solve the expression
function()