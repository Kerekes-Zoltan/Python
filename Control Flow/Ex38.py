"""
Write a Python program to display the astrological sign for a given date of birth.
Expected Output:

Input birthday: 15                                                      
Input month of birth (e.g. march, july etc): may                        
Your Astrological sign is : Taurus
"""

def get_astrological_sign(day, month):
    # Convert the month name to a numeric value
    month = month.lower()

    # Dictionary to map month names to numbers
    month_numbers = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5,
        'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10,
        'november': 11, 'december': 12
    }

    # Dictionary to map astrological signs and their date ranges
    signs = {
        'Capricorn': ((12, 22), (1, 19)),
        'Aquarius': ((1, 20), (2, 18)),
        'Pisces': ((2, 19), (3, 20)),
        'Aries': ((3, 21), (4, 19)),
        'Taurus': ((4, 20), (5, 20)),
        'Gemini': ((5, 21), (6, 20)),
        'Cancer': ((6, 21), (7, 22)),
        'Leo': ((7, 23), (8, 22)),
        'Virgo': ((8, 23), (9, 22)),
        'Libra': ((9, 23), (10, 22)),
        'Scorpio': ((10, 23), (11, 21)),
        'Sagittarius': ((11, 22), (12, 21)),
    }

    month_num = month_numbers.get(month)  # Get numeric value for the month
    if not month_num:
        return None  # If the month is invalid, return None

    for sign, ((start_month, start_day), (end_month, end_day)) in signs.items():
        # Check if birthdate falls within the range for the sign
        if (start_month == month_num and day >= start_day) or (end_month == month_num and day <= end_day):
            return sign

# Get user input
day = int(input("Input birthday (day): "))
month = input("Input month of birth (e.g. march, july etc.): ")

# Determine and print astrological sign
sign = get_astrological_sign(day, month)
if sign:
    print(f"Your Astrological sign is: {sign}")
else:
    print("Invalid month or day entered!")

