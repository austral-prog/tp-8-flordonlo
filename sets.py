from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    dish_ingred= set(dish_ingredients)
    dish= dish_name, dish_ingred
    return dish   

def check_drinks(drink_name, drink_ingredients):
    drink_ingred= set(drink_ingredients)
    if len(set(drink_ingred.intersection(ALCOHOLS))) != 0:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"
