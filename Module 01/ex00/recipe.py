"""
Let's describe the Recipe class. It has some attributes:
• name (str): name of the recipe,
• cooking_lvl (int): range from 1 to 5,
• cooking_time (int): in minutes (no negative numbers),
• ingredients (list): list of all ingredients each represented by a string,
• description (str): description of the recipe,
• recipe_type (str): can be "starter", "lunch" or "dessert".
"""

import random

class Recipe:
    """
    A class to handle the recipe
    """
    def __init__(self) -> None:
        """
        To be called automatically when Recipe class is instantiated.
        """
        self.name = ""
        self.cooking_lvl = random.randint(1, 5)
        self.cooking_time = 0
        self.ingredients = []
        self.description = ""
        self.recipe_type = "starter" or "lunch" or "dessert"

    def __str__(self):
        """
        Return the string to print with the recipe info
        """
        txt = (f"My Recipe\n"
        f"Recipe Name: {self.name}\n"
        f"Cooking Level: {self.cooking_lvl}\n"
        f"Cooking Time: {self.cooking_time}\n"
        f"Ingredients: {', '.join(self.ingredients)}\n"
        f"Description: {self.description}\n"
        f"Recipe Type: {self.recipe_type}")
        return txt
