"""
Write a Python program to remove the nth index character from a nonempty string.
"""

def remove_index_char(s, n):
    if n < 0 or n >= len(s):
        return 'Invalid String.'
    return s[:n] + s[n + 1:]

#Example usage
string = "Example"
n = 3
result = remove_index_char(string, n)

#Output
print("Original string:", string)
print("String after removing character at index", n, ":", result)