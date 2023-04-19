"""
The kata variable is always a tuple that contains 5 non-negative integers. The first
integer contains up to 4 digits, the rest up to 2 digits.
# Put this at the top of your kata02.py file
    kata = (2019, 9, 25, 3, 30)
Write a program that display this variable content according to the format shown
below:
$> python3 kata02.py | cat -e
09/25/2019 03:30$
$> python3 kata02.py | wc -c
17
"""
kata = (2019, 9, 25, 3, 30)
print(f"{kata[1]:02}/{kata[2]:02}/{kata[0]:04} {kata[3]:02}:{kata[4]:02}")
