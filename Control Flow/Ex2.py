"""
Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

#Fucntion to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

#Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main_program():
    print("Temperature Conversion")
    
    #Insert user data
    celsius_temp = int(input("Enter Celsius: "))
    fahrenheit_temp = int(input("Enter Fahrenheit: "))
    
    #Convert Celsius to Fahrenheit
    fahrenheit_result = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is {fahrenheit_result:.1f}°F")
    
    #Convert Fahrenheit to Celsius
    celsius_result = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is {celsius_result:.1f}°C")
    
if __name__ == '__main__':
    main_program()