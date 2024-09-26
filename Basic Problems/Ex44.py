"""
Write a Python program to locate Python site packages
"""

import site

def locate_python_packages():
    site_packages = site.getsitepackages()
    print("Python packages directories: ")
    
    for path in site_packages:
        print(path)
        
if __name__ == '__main__':
    locate_python_packages()