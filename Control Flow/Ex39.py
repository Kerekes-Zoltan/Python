"""
Write a Python program to display the sign of the Chinese Zodiac for the given year in which you were born.
Expected Output:

Input your birth year: 1973                                             
Your Zodiac sign : Ox
"""

def get_chinese_zodiac(year):
    
    #List of Chinese Zodiac signs corresponding to the 12-year cycle
    zodiac_sign = [
        'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
        'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig'
    ]
    
    #The cycle starts with 1924 as the Year of the Rat (Start of the current cycle)
    start_year = 1924
    cycle_position = (year - start_year) % 12
    
    return zodiac_sign[cycle_position]

#Prompt user input
year = int(input("Input your birth year: "))

#Determine and print Chinese Zodiac sign
zodiac_sign = get_chinese_zodiac(year)
print(f"Your zodiac sign: {zodiac_sign}")