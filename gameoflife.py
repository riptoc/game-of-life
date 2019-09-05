"""
    Conway's game of life in python
"""
import random

import pygame


def generate_gamestate(input):
    """
        Generate gamestate as 2d array from input
        eg. "#-##-" -> [1,0,1,1,0]
    """
    items = [[c for c in i] for i in input]
    return [[1 if i == "#" else 0 for i in j] for j in items]


def random_gamestate_input(row, col):
    """ Generate a random gamestate input give height/width """
    result = []

    for i in range(row):
        s = ""
        for j in range(col):
            s += random.choice(("#", "-"))
        result.append(s)

    return result


def import_gamestate(file):
    return [l.rstrip('\n') for l in open(file)]


def live_neighbours(row, col, gamestate):
    """ Count the live neighbours of a cell """
    num_rows = len(gamestate)
    num_cols = len(gamestate[0])
    total = 0
    i = -1
    while i < 2:
        # Count by row
        j = -1
        x = row + i
        # Wrap around
        if x >= num_rows:
            x = 0
        elif x == -1:
            x = num_rows - 1
        # Count each col
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


def get_next_gamestate(gs):
    """ Generate the next gamestate from the current one """
    return [[next_cellstate(j, live_neighbours(x, y, gs)) for y, j in enumerate(i)] for x, i in enumerate(gs)]


def next_cellstate(cellstate, num_neighbours):
    """Calculate a cell's next state based on number of live neighbours"""
    # If cell is alive
    if cellstate == 1:
        # Any live cell with two or three live neighbours lives
        if num_neighbours in [2, 3]:
            return 1
        # Any other state dies
        return 0
    # If cell is dead, any dead cell with exactly three live
    # neighbours becomes a live cell
    if num_neighbours == 3:
        return 1
    # Anything else stays dead
    return 0


# Main loop
def main():
    """ Main program starts here """
    gs_input = [
        "------",
        "-##---",
        "-##---",
        "---##-",
        "---##-",
        "------",
    ]
    gamestate = generate_gamestate(gs_input)

    # Random gamestate
    # gamestate = generate_gamestate(random_gamestate_input(64, 64))

    # Pygame setup
    pygame.init()
    framerate = 5
    # Screen size
    screen = pygame.display.set_mode((len(gamestate[0]) * 10, len(gamestate * 10)))
    # Initialise clock
    clock = pygame.time.Clock()
    # Colours
    bg = (200, 200, 200)
    fg = (50, 50, 50)
    # Cell sizes
    cell_w = 10
    cell_h = 10
    done = False
    while not done:
        # Event loop
        for event in pygame.event.get():
            # Press q to quit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                done = True

        # Set the bg colour
        screen.fill(bg)

        # Draw the cells
        i = 0
        while i < len(gamestate):
            j = 0
            while j < len(gamestate[0]):
                # Assign colours to each state
                colour = bg if gamestate[i][j] == 0 else fg
                # Draw next state to screen
                pygame.draw.rect(screen, colour, [j * 10, i * 10, cell_w, cell_h])
                j += 1
            i += 1
        # Update gamestate
        gamestate = get_next_gamestate(gamestate)

        # Update the screen
        pygame.display.flip()
        # Set the framerate
        clock.tick(framerate)

    # Exit pygame properly
    pygame.quit()


main()
