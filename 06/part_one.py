"""

"""
from typing import List


def solve_p1(answers: List[str]):
    total = 0
    yes_set = set()
    for answer in answers:
        if answer == "\n":
            total += len(yes_set)
            yes_set = set()
            continue
        for letter in answer.strip():
            yes_set.add(letter)

    total += len(yes_set)
    return total


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
