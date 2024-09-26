"""
 Write a Python program to check whether a file exists.
"""

import os

#Check file path
def check_file_exits(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False
    
#Example
file_path = input("Enter file path to check exists or not: ")

if check_file_exits(file_path):
    print(f"The file {file_path} exists.")
else:
    print(f"The file {file_path} DOES NOT exist.")