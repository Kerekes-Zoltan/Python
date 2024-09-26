"""
Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

def check_value_in_group(value, group):
    return value in group

#Get the value from the user
value = int(input("Enter the value to check: "))

#Get the group of values from the user(split by spaces and convert to integers)
group = list(map(int, input("Enter the group of values(separated by spaces: )").split()))

#Check if the value is in the group and print the result
result = check_value_in_group(value, group)
print(f"{value} -> {group} : {result}")