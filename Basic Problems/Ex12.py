"""Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module."""

import calendar

#Enter the year and month from user
year = int(input("Enter year: "))
month = int(input("Enter month: "))

#Create a calendar instance
calendar_data = calendar.TextCalendar(calendar.MONDAY)

#Generate the calendar for the given month and year
calendar_month = calendar_data.prmonth(year, month)

#Print the result
print(calendar_month)