"""
Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
"""
from typing import List


def solve_p1(raw_map: List[str]):
    total_trees = 0
    pointer = 0
    line_size = len(raw_map[0])
    for i in range(1, len(raw_map)):
        pointer += 3
        if pointer >= line_size - 1:
            pointer -= line_size - 1
        if raw_map[i][pointer] == "#":
            total_trees += 1

    return total_trees


def main():
    with open("test.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
