"""Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73"""

def calculate_dog_years(human_years):
    if human_years <= 2:
        #First two years: each equals 10.5 human years
        dog_years = human_years * 10.5
    else:
        #First two years = 21 dog years, subsequent years = 4 dog years each
        dog_years = 21 + (human_years - 2) * 4
    
    return dog_years

#Prompt user input
human_years = float(input("Input a dog's age in human years: "))

#Calculate Dog's age in dog years
dog_years = calculate_dog_years(human_years)

#Print result
print(f"The dog's age in dog's years is {int(dog_years)}")