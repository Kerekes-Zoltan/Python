"""Write a Python program to create the multiplication table (from 1 to 10) of a number.
Expected Output:

Input a number: 6                                                       
6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60
"""

def multiplication_table(value):
    print(f"Multiplication table for {value}: ")
    for i in range(1, 11):
        result = value * i
        print(f"{value} x {i} = {result}")
        
#Get user input
try:
    user_input = int(input("Input a number: "))
    multiplication_table(user_input)
except ValueError:
    print("Please enter a valid integer.")