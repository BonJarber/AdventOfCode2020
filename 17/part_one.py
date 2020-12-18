"""

"""
from copy import deepcopy
from pprint import pprint
from typing import List

# import numpy as np


def solve_p1(initial_state: List[str]):
    # grid = np.zeros((len(initial_state), len(initial_state[0]), 1), dtype=object)
    grid = []
    grid.append([])
    grid[0].append([])
    for i in range(0, len(initial_state)):
        grid.append([])
        for j in range(0, len(initial_state[i])):
            grid[i].append([])
            for k in range(0, 1):
                grid[i][j].append(initial_state[i][j])

    cycles = 1
    neighbors = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if not (x == 0 and y == 0 and z == 0):
                    neighbors.append((x, y, z))

    new_grid = deepcopy(grid)
    current_grid = None
    for cycle in range(0, cycles):
        current_grid = deepcopy(new_grid)

        # Add the neighboring blocks
        for x in range(0, len(current_grid)):
            current_grid.append([])
            for y in range(0, len(current_grid[x])):
                current_grid[x].append([])
                for z in range(0, len(current_grid[x][y])):
                    if len(current_grid[x][y]) < z:
                        current_grid[x][y].append(".")

        new_grid = deepcopy(current_grid)
        for x in range(0, len(current_grid)):
            for y in range(0, len(current_grid[x])):
                for z in range(0, len(current_grid[x][y])):
                    active = False
                    active_neighbors = 0
                    if current_grid[x][y][z] == "#":
                        active = True
                    for n in neighbors:
                        try:
                            if current_grid[x + n[0]][y + n[0]][z + n[0]] == "#":
                                active_neighbors += 1
                        except IndexError:
                            continue
                    if active and active_neighbors != 2 and active_neighbors != 3:
                        new_grid[x][y][z] = "."
                    else:
                        if active_neighbors == 3:
                            new_grid[x][y][z] = "#"


def main():
    with open("test.txt") as in_file:
        input_text = []
        for line in in_file.readlines():
            input_text.append(line.strip())
        return solve_p1(input_text)


if __name__ == "__main__":
    print(main())
