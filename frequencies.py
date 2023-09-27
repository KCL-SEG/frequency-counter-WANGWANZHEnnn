"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for item in items:
        # Convert the item to a string representation
        item_str = str(item)

        # Check if the item_str is already a key in the dictionary
        if item_str in frequencies:
            # Increment the count if the key already exists
            frequencies[item_str] += 1
        else:
            # Initialize the count to 1 if the key doesn't exist
            frequencies[item_str] = 1

    return frequencies





   
    