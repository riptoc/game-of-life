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

    return result


def count_neighbours(row, col, gamestate):
    """Count the live neighbours of a cell"""
    num_rows = len(gamestate)
    num_cols = len(gamestate[0])
    total = 0
    i = -1
    while i < 2:
        j = -1
        x = row + i
        if x >= num_rows:
            x = 0
        elif x == -1:
            x = num_rows - 1
        while j < 2:
            y = col + j
            if y >= num_cols:
                y = 0
            elif y == -1:
                y = num_cols - 1
            total += gamestate[x][y]
            j += 1
        i += 1
    total -= gamestate[row][col]
    return total
