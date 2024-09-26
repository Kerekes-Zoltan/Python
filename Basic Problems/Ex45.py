"""
Write a Python program that calls an external command.
"""


import subprocess
import platform

def call_external_command():
    
    #Check the operating system
    if platform.system() == 'Windows':
        #Use dir command for Windows
        command = ["cmd", "/c", "dir"]
    else:
        #Use 'ls' command for Linux
        command = ["ls", "-l"]
    
    try:
        #Run the external command
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        
        #Print the output of the command
        print("Command output: ")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occured: {e}")
        
if __name__ == '__main__':
    call_external_command()