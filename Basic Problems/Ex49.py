"""
Write a Python program to list all files in a directory.
"""

import os

def list_files_in_directory(directory):
    try:
        #List all files in the given directory
        files = os.listdir(directory)
        print(f"Files in '{directory}': ")
        
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Error: The direcotry '{directory}' does not exist.")
    except NotADirectoryError:
        print(f"Error: The path '{directory}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
        
if __name__ == '__main__':
    directory = input("Enter the directory path: ")
    list_files_in_directory(directory)