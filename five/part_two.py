"""

"""
from typing import List


def parse_seat(boarding_pass: str):
    row = [i for i in range(0, 128)]
    column = [i for i in range(0, 8)]
    for letter in boarding_pass:
        if letter == "F":
            row = row[: len(row) // 2]
        elif letter == "B":
            row = row[len(row) // 2 :]
        elif letter == "L":
            column = column[: len(column) // 2]
        elif letter == "R":
            column = column[len(column) // 2 :]

    seat_id = (row[0] * 8) + column[0]
    return seat_id


def solve_p2(boarding_passes: List[str]):
    seats = {i for i in range(11, 836)}
    for boarding_pass in boarding_passes:
        seat_id = parse_seat(boarding_pass.strip())
        seats.remove(seat_id)

    return seats


def main():
    with open("input.txt") as in_file:
        return solve_p2(in_file.readlines())


if __name__ == "__main__":
    print(main())
