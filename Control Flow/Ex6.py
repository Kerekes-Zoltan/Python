"""Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""
#Function to count even numbers
def count_even_number(numbers):
    cnt_even = 0
    
    for i in numbers:
        if i % 2 == 0:
            cnt_even += 1
    return cnt_even

#Function to count odd numbers
def count_odd_number(numbers):
    cnt_odd = 0
    
    for i in numbers:
        if i % 2 != 0:
            cnt_odd += 1
    return cnt_odd

def main():
    # Prompt user to enter a series of numbers
    user_input = input("Enter the series of numbers separated by space or comma: ")
    
    # Replace commas with spaces, then split the input string
    data = list(map(int, user_input.replace(',', ' ').split()))
    
    #Print out both even and odd counts
    print(f"Number of even numbers: {count_even_number(data)}")
    print(f"Number of odd numbers: {count_odd_number(data)}")
    
if __name__ == '__main__':
    main()