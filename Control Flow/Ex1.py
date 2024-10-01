"""
Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
"""

def find_divisible_by_7_and_multiple_of_5():
    
    result = []
    for i in range(1500, 2700):
        if i % 7 == 0 and i % 5 == 0:
            result.append(i)
    return result
            
#Get the numbers
numbers = find_divisible_by_7_and_multiple_of_5()

print(f"Numbers divisible by 7 and multiples of 5 between 1500 and 2700 are: {numbers}")