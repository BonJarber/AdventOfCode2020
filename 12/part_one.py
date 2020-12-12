"""

"""
from typing import List


def solve_p1(instructions: List[str]):
    orientation = 90
    e_w = 0
    n_s = 0
    for instruction in instructions:
        command = instruction[0]
        value = int(instruction[1:])
        if command == "N":
            n_s += value
        elif command == "S":
            n_s -= value
        elif command == "E":
            e_w += value
        elif command == "W":
            e_w -= value
        elif command == "L":
            orientation -= value
            while orientation < 0:
                orientation += 360
            while orientation > 360:
                orientation -= 360
        elif command == "R":
            orientation += value
            while orientation > 360:
                orientation -= 360
            while orientation < 0:
                orientation += 360
        elif command == "F":
            if orientation > 0 and orientation <= 90:
                e_w += value
            elif orientation > 90 and orientation <= 180:
                n_s -= value
            elif orientation > 180 and orientation <= 270:
                e_w -= value
            else:
                n_s += value

    return abs(e_w) + abs(n_s)


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
