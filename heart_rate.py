"""
heart_rate.py - A program to compute and output the slowest and fastest heart rates necessary to strengthen the heart.
"""

# Get the user's age as a string.
text = input("Please enter your age: ")

# Convert the string that the user entered into an integer.
age = int(text)

# Compute the slowest and fastest beneficial heart rates from the user's age.
max_rate = 220 - age
slowest = max_rate * 0.65
fastest = max_rate * 0.85

# Use an f-string to create and print a message for the user to see.
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.")
