"""
Write a Python program to print the alphabet pattern 'A'.
Expected Output:
  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *
"""

def print_pattern_A():
    pattern = [
        "  ***  ",
        " *   * ",
        " *   * ",
        " ***** ",
        " *   * ",
        " *   * ",
        " *   * "
    ]
    
    #Print each line of the pattern
    for line in pattern:
        print(line)
        
#Call the function to print the pattern
print_pattern_A()