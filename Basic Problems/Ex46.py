"""
Write a Python program to retrieve the path and name of the file currently being executed.
"""

from pathlib import Path

def get_current_path():
    
    #Get the full path of the current file
    full_path = Path(__file__).resolve()
    
    #Get the directory and the file name separately
    file_directory = full_path.parent
    file_name = full_path.name
    
    print(f"Full path: {full_path}")
    print(f"File Directory: {file_directory}")
    print(f"File Name: {file_name}")
    
if __name__ == '__main__':
    get_current_path()