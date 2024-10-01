"""Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days"""

def check_days_in_month(user_input):
    months = {
        'January': '31 days',
        'February': '28/29 days',
        'March': '31 days',
        'April': '30 days',
        'Mai': '31 days',
        'June': '30 days',
        'July': '31 days',
        'August': '31 days',
        'September': '30 days',
        'October': '31 days',
        'November': '30 days',
        'December': '31 days'
    }
    #Return the number of days if the month is valid, else an error message is displayed
    return months.get(user_input, "Invalid input. Please write a months name.")

#Input from user
user_input = input("Input the name of Month")

#Get the number of days for the input month and print the result
days = check_days_in_month(user_input)
print(f"No. of days: {days}")