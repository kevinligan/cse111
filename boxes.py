"""
boxes.py - A program to calculate the number of boxes needed to pack items based on user input.
"""

# Get the number of items and items per box from the user.
num_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# Calculate the number of boxes needed.
num_boxes = (num_items + items_per_box - 1) // items_per_box

# Display the result to the user.
print(f"For {num_items} items, packing {items_per_box} items in each box, you will need {num_boxes} boxes.")
