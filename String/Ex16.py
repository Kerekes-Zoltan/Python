"""
Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""

def insert_sting_middle(data1, data2):
    middle = len(data1) // 2
    return data1[:middle] + data2 + data1[middle:]

#Example usage
print(insert_sting_middle('[[]]<<>>', 'Python')) # Output: [[Python]]
print(insert_string_middle('{{}}', 'PHP'))  # Output: {{PHP}}