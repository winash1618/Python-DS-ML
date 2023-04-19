"""
The kata variable is always a string whose length is not higher than 42.
# Put this at the top of your kata03.py file
kata = "The right format"
Write a program that display this variable content according to the format shown
below:
$> python3 kata03.py | cat -e
--------------------------The right format%
$> python3 kata03.py | wc -c
42
$>
"""
kata = "The right format"
kata_new = kata.rjust(42, "-")
print(kata_new)