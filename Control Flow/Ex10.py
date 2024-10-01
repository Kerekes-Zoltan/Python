"""Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz
"""

# Iterate over integers from 1 to 50
for number in range(1, 51):
    # Check if the number is divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Check if the number is divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # Check if the number is divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # If the number is not divisible by 3 or 5, print the number itself
    else:
        print(number)
