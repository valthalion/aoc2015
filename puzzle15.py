from math import prod
from typing import NamedTuple


class Features(NamedTuple):
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


testing = False


def read_data():
    filename = 'puzzle15_test.in' if testing else 'puzzle15.in'
    ingredients = {}
    with open(filename, 'r') as f:
        for line in f:
            name, feature_spec = line.strip().split(': ')
            features = (int(feature.split()[1]) for feature in  feature_spec.split(', '))
            ingredients[name] = Features(*features)
    return ingredients


def score(ingredients, recipe, calories=None):
    totals = (0, 0, 0, 0, 0)
    for ingredient, amount in zip(ingredients.keys(), recipe):
        totals = tuple(prev + amount * value for prev, value in zip(totals, ingredients[ingredient]))
    totals = tuple(total if total >= 0 else 0 for total in totals)
    if calories is not None and totals[-1] != calories:
        return 0
    return prod(totals[:-1])


def best_recipe(ingredients, total=100, calories=None, base_recipe=tuple()):
    current_ingredient = len(base_recipe)
    if current_ingredient == len(ingredients) - 1:
        recipe = (*base_recipe, total)
        return score(ingredients, recipe, calories=calories)
    return max(
        best_recipe(ingredients, total=total - amount, calories=calories, base_recipe=(*base_recipe, amount))
        for amount in range(total + 1)
    )


def part_1():
    ingredients = read_data()
    return best_recipe(ingredients)


def part_2():
    ingredients = read_data()
    return best_recipe(ingredients, calories=500)
