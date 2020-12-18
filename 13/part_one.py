"""

"""
from typing import List


def solve_p1(puzzle_input: List[str]):
    your_time = int(puzzle_input[0].strip())
    buses = puzzle_input[1].strip().split(",")
    bus_to_take = None

    for bus in buses:
        if bus != "x":
            arrival_time = (your_time // int(bus)) * int(bus)
            if arrival_time < your_time:
                arrival_time += int(bus)

            if not bus_to_take or arrival_time < bus_to_take[0]:
                bus_to_take = (arrival_time, int(bus))

    wait_time = bus_to_take[0] - your_time
    return wait_time * bus_to_take[1]


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
