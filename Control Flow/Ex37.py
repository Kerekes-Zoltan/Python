"""
Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
Expected Output:

Input the month (e.g. January, February etc.): july                     
Input the day: 31                                                       
Season is autumn 
"""

#Function to determine the season based on month and day
def find_season(month, day):
    
    #Convert month to lowercase to handle case insesitivity
    month = month.lower()
    
    #check for each season based on the month and day
    if (month == "december" and day >= 21) or month in ["january", "february"] or (month == "march" and day < 20):
        return "Winter"
    elif (month == "march" and day >= 20) or month in ["april", "may"] or (month == "june" and day < 21):
        return "Spring"
    elif (month == "june" and day >= 21) or month in ["july", "august"] or (month == "september" and day < 23):
        return "Summer"
    elif (month == "september" and day >= 23) or month in ["october", "november"] or (month == "december" and day < 21):
        return "Autumn"
    else:
        return "Invalid date"
    
#Input the month and day from the user
month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

#Call the function to get the season
season = find_season(month, day)

#Print the season
print(f"Season is: {season.lower()}")