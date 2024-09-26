"""
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""

import struct

def check_python_bits():
    bits = struct.calcsize("P") * 8
    return bits

#Print data
bits = check_python_bits()
print(f"The Python shell is runnig is {bits}-bit mode.")