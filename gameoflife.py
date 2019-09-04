"""
    Conway's game of life in python
"""


def generate_gamestate(input):
    """
        Generate gamestate as 2d array from input
        eg. "# ## " -> [1,0,1,1,0]
    """
    items = [[c for c in i] for i in input]
    return [[1 if i == "#" else 0 for i in j] for j in items]
