"""Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import datetime

#Sample dates
date1 = (2014, 7, 2)
date2 = (2014, 7, 11)

#Convert tuples to objects
date1 = datetime(*date1)
date2 = datetime(*date2)

#Calculate the difference between the two dates
difference = date2 - date1

#Extract the number of days from the difference
days_between = difference.days

#Print the difference
print(f"{days_between} days")