"""

"""
from typing import List


def solve_p2(puzzle_input: List[str]):
    buses = puzzle_input[1].strip().split(",")
    bus_ordering = []

    for i in range(0, len(buses)):
        if buses[i] != "x":
            bus_ordering.append((i, int(buses[i])))

    success = False
    t = bus_ordering[0][1]
    while not success:
        is_solution = True
        for delta, bus in bus_ordering:
            if (t + delta) % bus != 0:
                is_solution = False

        if is_solution:
            success = True
        else:
            t += bus_ordering[0][1]

    return t


def main():
    with open("input.txt") as in_file:
        return solve_p2(in_file.readlines())


if __name__ == "__main__":
    print(main())
