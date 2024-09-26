"""
 Write a Python program to get OS name, platform and release information.
"""

import os
import platform

def system_information():
    #Get OS name
    os_name = os.name
    
    #Get platform and release information
    platform_system = platform.system() #Linux, MacOS, Windows, etc...
    platform_release = platform.release() #OS release version
    
    return os_name, platform_system, platform_release

#Example usage
os_name, platform_system, platform_release = system_information()
print(f"OS Name: {os_name}")
print(f"Platform System: {platform_system}")
print(f"Platform Release: {platform_release}")