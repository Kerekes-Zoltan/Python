"""
Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""

#Input for number of rows and columns
rows = int(input("Enter Rows: "))
columns = int(input("Enter columns: "))
    
#Initialize an empty list to hold the 2D array
array = []
    
#Create array
for i in range(rows):
    #Create a row with i*j
    row = []
    for j in range(columns):
        row.append(i * j)
        
    #Append the row to the array
    array.append(row)
        
#Print the resulting 2D array
print("Generated 2D array: ", array)