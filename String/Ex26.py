"""
Write a Python program to display formatted text (width=50) as output.
"""

import textwrap

def format_text(text, width):
    formatted_text = textwrap.fill(text, width)
    return formatted_text



if __name__ == "__main__":
    user_width = int(input("Enter the desired text width: "))
    user_input = input("Enter the desired text: ")
    print(format_text(user_input, user_width))