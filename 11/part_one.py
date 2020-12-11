"""

"""
import copy
from typing import List


def solve_p1(seat_input: List[str]):
    new_grid = []
    for row in seat_input:
        new_grid.append(list(row.strip()))

    changes = None

    while changes != 0:
        changes = 0
        grid = new_grid
        new_grid = copy.deepcopy(grid)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                current_space = grid[i][j]
                surrounding_spaces = [
                    (i, j + 1),
                    (i, j - 1),
                    (i + 1, j),
                    (i - 1, j),
                    (i + 1, j + 1),
                    (i - 1, j - 1),
                    (i + 1, j - 1),
                    (i - 1, j + 1),
                ]
                if current_space == "L":
                    occupied_nearby = False
                    for s in surrounding_spaces:
                        if s[0] >= 0 and s[1] >= 0:
                            try:
                                if grid[s[0]][s[1]] == "#":
                                    occupied_nearby = True
                            except IndexError:
                                pass
                    if not occupied_nearby:
                        new_grid[i][j] = "#"
                        changes += 1
                elif current_space == "#":
                    total_nearby = 0
                    for s in surrounding_spaces:
                        if s[0] >= 0 and s[1] >= 0:
                            try:
                                if grid[s[0]][s[1]] == "#":
                                    total_nearby += 1
                            except IndexError:
                                pass
                    if total_nearby >= 4:
                        new_grid[i][j] = "L"
                        changes += 1

    total_empty = 0
    for row in new_grid:
        total_empty += sum(s.count("#") for s in row)

    return total_empty


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
