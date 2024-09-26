"""Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""

#Enter filename from user
filename = input("Enter the file name: ")

#split the file name by the '.'
file_extension = filename.split('.')[-1]

#Print the file
print("File extension: ", file_extension)
