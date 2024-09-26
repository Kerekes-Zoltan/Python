"""
Write a Python program to find out the number of CPUs used.
"""

import os

def cpu_count():
    cpu_count = os.cpu_count()
    print(f"Number of CPU's used: {cpu_count}")
    
if __name__ == '__main__':
    cpu_count()