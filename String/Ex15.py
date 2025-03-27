"""
Write a Python function to create an HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""

def add_tags(tag, data):
    return f'<{tag}>{data}</{tag}>'

#Example usage
print(add_tags('i', 'Python')) #Output: <i>Python<i>
print(add_tags('b', 'Python Tutorial')) #Output: <b>Python Tutorial</b>