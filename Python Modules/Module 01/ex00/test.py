"""
Finally, you will provide a test.py file to test your classes and prove that they are
working properly. You can import all the classes into your test.py file by adding these
lines at the top of the test.py file:
"""
from datetime import datetime
from book import Book
from recipe import Recipe

myBook = Book()
myBook.name = input("Please enter the recipe book name")
try:
    if not myBook.name:
        raise ValueError("Input is empty")
except ValueError as e:
    print(e)
myBook.creation_date = datetime.now()
myBook.last_update = datetime.now()

while True:
    print(f"Welcome to the {myBook.name}!")
    print("Please enter one of the available options: ")
    print("    1. add a recipe")
    print("    2. get recipes by name")
    print("    3. get recipes by type")
    print("    4. exit")
    choice = input("Enter you choice: ")
    if choice == '1':
        myRecipe = Recipe()
        try:
            myRecipe.name = input("Enter your recipe name: ")
            if not myRecipe.name:
                raise ValueError("Input is empty")
            myRecipe.cooking_lvl = int(input("Enter your recipe cooking level: "))
            if myRecipe.cooking_lvl < 1 and myRecipe.cooking_lvl > 5:
                raise ValueError("cooking lvl out of range, cooking lvl [1, 5]")
            myRecipe.cooking_time = int(input("Enter your recipe cooking time: "))
            if myRecipe.cooking_time < 0:
                raise ValueError("cooking time should be positive number")
            while True:
                ingredient = input("Enter ingredient (or leave empty to stop): ")
                if not ingredient:
                    break
                myRecipe.ingredients.append(ingredient)
            if len(myRecipe.ingredients) == 0:
                raise ValueError("recipe should have atleast one ingredient.")
            myRecipe.description = input("Enter description for the recipe")
            myRecipe.recipe_type = input("Enter recipe type, options available"
                                         " (starter, lunch, dessert)")
            if not any(myRecipe.recipe_type in s for s in ["starter", "lunch", "dessert"]):
                raise ValueError("recipe type should be starter or lunch or dessert")
        except ValueError as e:
            print(e)
            continue
        except KeyError as k:
            print(k)
            continue
        myBook.add_recipe(myRecipe)
        myBook.last_update = datetime.now()
    elif choice == '2':
        try:
            recipe_name = input("Enter the name of the recipe you want to get")
            if not recipe_name:
                raise ValueError("recipe name can't be empty")
        except ValueError as e:
            print(e)
            continue
        newRecipe = myBook.get_recipe_by_name(recipe_name)
        print(str(newRecipe))
    elif choice == '3':
        try:
            recipe_type = input("Enter recipe type to get the recipes,"
                                " options available (starter, lunch, dessert)")
            if not any(recipe_type in s for s in ["starter", "lunch", "dessert"]):
                raise ValueError("recipe type should be starter or lunch or dessert")
        except ValueError as e:
            print(e)
            continue
        recipe_list = myBook.get_recipes_by_types(recipe_type)
        print(recipe_list)
    elif choice == '4':
        exit(1)
    else:
        print("Please enter the correct choice")
        continue
