"""
Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
"""
from functools import reduce
from typing import List, Tuple


def solve_p2(raw_map: List[str], slopes: List[Tuple[int]]):
    total_trees = []
    line_size = len(raw_map[0])
    for i in range(0, len(slopes)):
        over = slopes[i][0]
        down = slopes[i][1]
        pointer = 0
        total_trees.append(0)
        for j in range(down, len(raw_map), down):
            pointer += over
            if pointer >= line_size - 1:
                pointer -= line_size - 1
            if raw_map[j][pointer] == "#":
                total_trees[i] += 1

    return reduce(lambda x, y: x * y, total_trees)


def main():
    with open("input.txt") as in_file:
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        return solve_p2(in_file.readlines(), slopes)


if __name__ == "__main__":
    print(main())
