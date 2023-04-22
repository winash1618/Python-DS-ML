"""
The Book class also has some attributes:
• name (str): name of the book,
• last_update (datetime): the date of the last update,
• creation_date (datetime): the creation date,
• recipes_list (dict): a dictionnary with 3 keys: "starter", "lunch", "dessert"
"""
import datetime

class Book:
    """
    The Book class that contain all the recipes
    """
    def __init__(self) -> None:
        self.name = ""
        self.last_update = datetime
        self.creation_date = datetime
        self.recipes_list = {'lunch': [], 'dessert': [], 'starter': []}

    def get_recipe_by_name(self, name) -> any:
        """
        Prints a recipe with the name \texttt{name} and returns the instance
        """
        for values in self.recipes_list.values():
            for recipe in values:
                if recipe.name == name:
                    return recipe
        print("No recipe in that name")

    def get_recipes_by_types(self, recipe_type) -> any:
        """
        Get all recipe names for a given recipe_type
        """
        recipe_names = []
        for key, recipes in self.recipes_list.items():
            if key == recipe_type:
                for recipe in recipes:
                    recipe_names.append(recipe.name)
        if len(recipe_names) == 0:
            print("No recipes for that type")
        else:
            return recipe_names

    def add_recipe(self, recipe):
        """
        Add a recipe to the book and update last_update
        """
        self.recipes_list[recipe.recipe_type].append(recipe)
