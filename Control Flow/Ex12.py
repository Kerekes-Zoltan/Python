"""
Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
"""

def collect_and_print_lines():
    
    lines = []
    print("Enter text (press Enter on a blank line to terminate): ")
    
    #Accept input from the user line by line
    while True:
        line = input()  #Read a line of input
        if line == '':  #check if the line is blank
            break       #Exit the loop if the line is blank
        lines.append(line.lower())  #Convert the line to lowercase and add to the list
        
    #Output all the collected lines
    print("\nYou entered the following lines: ")
    for line in lines:
        print(line)
        
if __name__ == '__main__':
    collect_and_print_lines()