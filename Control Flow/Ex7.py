"""
Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
"""

def prints_type_for_item():
    # Predefined datalist
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
    
    # Loop through each item in the list and print the item and its type
    for item in datalist:
        print(f"Item: {item}, Type: {type(item)}")
        
if __name__ == '__main__':
    prints_type_for_item()