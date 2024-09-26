"""
Write a Python program that displays your name, age, and address on three different lines.
"""

#Function to display Name, Age, Address
def display_personal_information(name, age, address):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Address: {address}")
    
#Define variables
name = "John Doe"       # Replace with your name
age = 25                # Replace with your age
address = "Str. 1Noiembrie, Bistrița"  # Replace with your address

#call function to display information
display_personal_information(name, age, address)