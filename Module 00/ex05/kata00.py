"""
The kata variable is always a tuple and can only be filled with integer.
# Put this at the top of your kata00.py file
    kata = (19,42,21)
Write a program that display this variable content according to the format shown
below:
$> python3 kata00.py
    The 3 numbers are: 19, 42, 21
"""
kata = (19,42,21)
print(f"The {len(kata)} numbers are: {kata[0]}, {kata[1]}, {kata[2]}")
