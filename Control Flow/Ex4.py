"""Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
def create_pattern():
    #Promt the user to enter a number
    number = int(input("Enter a number: ")) 
    
    #First half of the pattern
    for i in range(1, number + 1):
        print('* ' * i)
        
    #Second half of the pattern
    for i in range(number - 1, 0, -1):
        print('* ' * i)
    
    return

if __name__ == '__main__':
    create_pattern()
    