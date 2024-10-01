"""
Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
"""


def calculate_sum_and_average():
    # Initialize variables
    total_sum = 0
    count = 0

    print("Enter integer numbers (Input 0 to finish):")

    while True:
        number = int(input())  # Take input from the user
        if number == 0:  # Exit the loop when 0 is entered
            break
        total_sum += number  # Add number to the sum
        count += 1  # Increase count of numbers

    if count == 0:
        print("No numbers were entered.")
    else:
        average = total_sum / count  # Calculate average
        print(f"Sum: {total_sum}")
        print(f"Average: {average}")

# Call the function
calculate_sum_and_average()
