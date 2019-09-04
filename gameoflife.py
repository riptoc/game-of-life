"""
    Conway's game of life in python
"""
import random


def generate_gamestate(input):
    """
        Generate gamestate as 2d array from input
        eg. "# ## " -> [1,0,1,1,0]
    """
    items = [[c for c in i] for i in input]
    return [[1 if i == "#" else 0 for i in j] for j in items]


def random_gamestate_input(row, col):
    result = []

    for i in range(row):
        s = ""
        for j in range(col):
            s += random.choice(("#", " "))
        result.append(s)
    print(result)
    return result
