"""
Part 1: Nested Dictionaries
	- https://www.programiz.com/python-programming/nested-dictionary
Part 2: A series of Helpful Functions
	- Create a series of useful functions to handle your cookbook:
		1. A function that print all recipe names.
		2. A function that takes a recipe name and print its details.
		3. A function that takes a recipe name and delete it.
		4. A function that add a recipe from user input. You will need a name, a list of 
		ingredient, a meal type and a preparation time.
"""

cookbook = {
    'Sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                 'meal': 'lunch', 'prep_time': 10},
    'Cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'desert', 'prep_time': 60},
    'Salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
              'meal': 'lunch', 'prep_time': 15}
}


def print_cookbook() -> None:
    """
    For printing the cookbook dictionary
    """
    for recipe in cookbook.items():
        print(recipe)


def print_recipe() -> None:
    """
    For printing all details of the recipe
    """
    recipe_name = input("Please enter a recipe name to get its details:")
    try:
        cookbook[recipe_name]
    except KeyError:
        print("recipe name is not in the list")
        return
    print(f"recipe for {recipe_name}")
    print(f"    Ingredients list: {cookbook[recipe_name]['ingredients']}")
    print(f"    To be eaten for {cookbook[recipe_name]['meal']}.")
    print(f"    Takes {cookbook[recipe_name]['prep_time']} minutes of cooking.")


def delete_recipe() -> None:
    """
    For deleting a recipe from the cookbook
    """
    recipe_name = input("Please enter a recipe name to delete:")
    try:
        cookbook[recipe_name]
    except KeyError:
        print("recipe name is not in the list")
        return
    del cookbook[recipe_name]


def add_recipe() -> any:
    """
    For creating a new recipe and add it to the cookbook
    """
    recipe_name = input("Enter a name: ")
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient: ")
        if ingredient == "":
            break
        ingredients.append(ingredient)
    meal = input("Enter a meal type: ")
    prep_time = input("Enter a preparation time: ")
    cookbook[recipe_name] = {'ingredients': ingredients,
                             'meal': meal, 'prep_time': int(prep_time)}


if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    while True:
        print("List of available option:")
        for value in ["    1: Add a recipe", "    2: Delete a recipe",
                      "    3: Print a recipe", "    4: Print the cookbook", "    5: Quit"]:
            print(f"{value.ljust(25, ' ')}")
        choice = input("Please select an option:\n>> ")
        if choice == '1':
            add_recipe()
        elif choice == '2':
            delete_recipe()
        elif choice == '3':
            print_recipe()
        elif choice == '4':
            print_cookbook()
        elif choice == '5':
            print("Cookbook closed. Goodbye !")
            exit(1)
        else:
            print("Sorry, this option does not exist")
