"""

"""
import math
from typing import List


def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return round(qx), round(qy)


def solve_p2(instructions: List[str]):
    wp_e_w = 10
    wp_n_s = 1
    sp_e_w = 0
    sp_n_s = 0
    for instruction in instructions:
        command = instruction[0]
        value = int(instruction[1:])
        if command == "N":
            wp_n_s += value
        elif command == "S":
            wp_n_s -= value
        elif command == "E":
            wp_e_w += value
        elif command == "W":
            wp_e_w -= value
        elif command == "L":
            wp_e_w, wp_n_s = rotate((0, 0), (wp_e_w, wp_n_s), math.radians(value))
        elif command == "R":
            wp_e_w, wp_n_s = rotate((0, 0), (wp_e_w, wp_n_s), math.radians(value * -1))
        elif command == "F":
            for _ in range(value):
                sp_e_w += wp_e_w
                sp_n_s += wp_n_s
    return abs(sp_e_w) + abs(sp_n_s)


def main():
    with open("input.txt") as in_file:
        return solve_p2(in_file.readlines())


if __name__ == "__main__":
    print(main())
