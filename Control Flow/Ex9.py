"""
Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
"""
#Initialize the first two Fiboonacci numbers
a, b = 0, 1

#Create the list to store Fibonacci numbers
fibonacci_numbers = []

#Generate Fibonacci numbers until the next number exceed 50
while b <= 50:
    #Append to the list if it is greater than 0
    if b > 0:
        fibonacci_numbers.append(b)
        
    #Update the Fibonacci numbers
    a, b = b, a + b
    
#Print the Fibonacci series
print("Fibonacci series between 0 and 50: ", " ".join(map(str, fibonacci_numbers)))