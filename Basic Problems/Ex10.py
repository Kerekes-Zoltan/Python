"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

#Define intege (N)
input_data = input("Enter value of N: ")

#Compute the value of N + NN + NNN
result = int(input_data) + int(input_data*2) + int(input_data*3)

#Print the result
print("The reuslt is:", result)