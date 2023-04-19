"""
The kata variable is always a dictionary and can only be filled with strings.
# Put this at the top of your kata01.py file
kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}
Write a program that display this variable content according to the format shown
below:
$> python3 kata01.py
Python was created by Guido van Rossum
Ruby was created by Yukihiro Matsumoto
PHP was created by Rasmus Lerdorf
"""
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
for key, value in kata.items():
    print(f"{key} was created by {value}")
