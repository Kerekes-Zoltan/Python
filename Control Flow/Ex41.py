"""
Write a Python program to get the next day of a given date.
Expected Output:

Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23                                                  
The next date is [yyyy-mm-dd] 2016-8-24   
"""

def is_leap_year(year):
    #Check if the year is a leap year
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def get_next_day(year, month, day):
    #Day in each month(index 1 for Fanuary to 12 for December)
    month_days = [31,29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #Check if it's the last day of the month
    if day < month_days[month - 1]:
        day += 1
    else:
        #If it's the last day of the month, reset day and move to the next month
        day = 1
        if month == 12:
            #If it's December, roll over to teh enxt year
            month = 1
            year += 1
        else:
            #Otherwise, just move to the next month
            month += 1
            
    return year, month, day

#Prompt user to input
year = int(input("Input a year: "))
month = int(input("Input a month [1 - 12]: "))
day = int(input("Input a day [1 - 31]: "))

#Find the next day
next_year, next_month, next_day = get_next_day(year, month, day)

#Print the next date in the format [yyyy-mm-dd]
print(f"The next date is [yyyy-mm-dd] {next_year}-{next_month}-{next_day}")