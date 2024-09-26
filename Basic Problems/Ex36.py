"""
Write a Python program to add two objects if both objects are integers.
"""

#Define the function
def add_objects_integers(object_1, object_2):
    #Check if both A and B are integers
    if isinstance(object_1, int) and isinstance(object_2, int):
        return object_1 + object_2
    else:
        return "Both inputs must be integers"
    
def main():
    #Prompt user for input
    try:
        object_1 = input("Enter the first object: ")
        object_2 = input("Enter the second object: ")
        
        #Convert inputs to integers
        object_1 = int(object_1) if object_1.isdigit() or (object_1[1:].isdigit() and object_1[0] == '-') else object_1
        object_2 = int(object_2) if object_2.isdigit() or (object_2[1:].isdigit() and object_2[0] == '-') else object_2
        
        result = add_objects_integers(object_1, object_2)
        print(f"{result}")
        
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        
if __name__ == '__main__':
    main()