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
                directions = [
                    (1, 0),  # Down
                    (-1, 0),  # Up
                    (0, 1),  # Right
                    (0, -1),  # Left
                    (1, 1),  # Down and to the right
                    (-1, 1),  # Up and to the right
                    (-1, -1),  # Up and to the left
                    (1, -1),  # Down and to the left
                ]
                surrounding_spaces = set()
                for direction in directions:
                    keep_looking = True
                    x = i
                    y = j
                    while keep_looking:
                        x += direction[0]
                        y += direction[1]
                        if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[i]):
                            checked_space = grid[x][y]
                            surrounding_spaces.add((x, y))
                            if checked_space != ".":
                                keep_looking = False
                        else:
                            keep_looking = False
                if current_space == "L":
                    occupied_nearby = False
                    for s in surrounding_spaces:
                        if grid[s[0]][s[1]] == "#":
                            occupied_nearby = True
                    if not occupied_nearby:
                        new_grid[i][j] = "#"
                        changes += 1
                elif current_space == "#":
                    total_nearby = 0
                    for s in surrounding_spaces:
                        if grid[s[0]][s[1]] == "#":
                            total_nearby += 1
                    if total_nearby >= 5:
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
