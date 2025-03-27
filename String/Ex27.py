"""
Write a Python program to remove existing indentation from all of the lines in a given text.
"""

import textwrap

def remove_indentation(text):
    return textwrap.dedent(text)

sample_text = """    
        Python is an interpreted, high-level, general-purpose 
        programming language. Its design philosophy emphasizes 
        code readability with its notable use of significant indentation.
    """

cleaned_text = remove_indentation(sample_text)

print(cleaned_text)