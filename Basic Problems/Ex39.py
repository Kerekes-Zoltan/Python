"""
Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

#Function to calculate future value
def future_value(principal, rate_of_interest, years):
    
    #Compound interest formula
    future_value = principal * (1 + (rate_of_interest / 100)) ** years
    
    #Rounding to two decimal places for currency representation
    return round(future_value, 2)

# Given data
principal = 10000  # Principal amount
rate_of_interest = 3.5       # Interest rate per year (in %)
years = 7                 # Number of years

#Calculate future value
future_v = future_value(principal, rate_of_interest, years)

#Print result with 2 decimals
print(f"Future value: {future_v}")