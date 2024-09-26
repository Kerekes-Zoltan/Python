"""Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""

def print_different_color():
    #Input from the user and convert it into a list of colors
    colorlist1 = set(input("Enter list 1, separated by ',': ").split(','))
    colorlist2 = set(input("Enter list 2, separated by a ',':").split(','))
    
    #Find colors in colorlist1 that are not in colorlist2
    difference = colorlist1.difference(colorlist2)
    
    #Print the result
    print("Colors in list 1, but NOT in list 2: ", difference)

#Call the function
print_different_color()