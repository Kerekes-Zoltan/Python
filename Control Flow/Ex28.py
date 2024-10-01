"""
Write a Python program to print the following patterns.
Expected Output:

  ****                                                                  
 *                                                                      
 *                                                                      
  ***                                                                   
     *                                                                  
     *                                                                  
 **** 
 
 ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
oooo                                                                    
oooo                                                                    
oooo                                                                    
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
             oooo                                                       
             oooo                                                       
             oooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo 
"""

def print_pattern_1():
    pattern = [
        "  ****  ",
        " *      ",
        " *      ",
        "  ***   ",
        "     *  ",
        "     *  ",
        " ****   "
    ]
    
    for line in pattern:
        print(line)

def print_pattern_2():
    pattern = [
        " ooooooooooooooooo ",
        "ooooooooooooooooo",
        "ooooooooooooooooo",
        "oooo            ",
        "oooo            ",
        "oooo            ",
        "ooooooooooooooooo",
        "ooooooooooooooooo",
        "ooooooooooooooooo",
        "            oooo",
        "            oooo",
        "            oooo",
        "ooooooooooooooooo",
        "ooooooooooooooooo",
        "ooooooooooooooooo"
    ]
    
    for line in pattern:
        print(line)

# Call the functions to print both patterns
print("Pattern 1:")
print_pattern_1()
print("\nPattern 2:")
print_pattern_2()
