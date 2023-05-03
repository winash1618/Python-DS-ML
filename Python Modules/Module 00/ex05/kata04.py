"""
The kata variable is always a tuple that contains, in the following order:
	• 2 non-negative integer containing up to 2 digits
	• 1 decimal
	• 1 integer
	• 1 decimal
# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)
Write a program that display this variable content according to the format shown
below:
$> python3 kata04.py
module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
$> python3 kata04.py | cut -c 10,18
,:
"""
kata = (0, 4, 132.42222, 10000, 12345.67)
print(f"module_{kata[0]:02}, ex_{kata[1]:02} : {round(kata[2], 2)}, {kata[3]:.2e}, {kata[4]:.2e}")
