"""

"""
from typing import List


def solve_p2(answers: List[str]):
    total = 0
    group_size = 0
    yes_dict = {}
    for answer in answers:
        if answer == "\n":
            for key in yes_dict.keys():
                if yes_dict[key] == group_size:
                    total += 1
            yes_dict = {}
            group_size = 0
            continue
        group_size += 1
        for letter in answer.strip():
            if letter in yes_dict:
                yes_dict[letter] += 1
            else:
                yes_dict[letter] = 1

    total += len(yes_dict)
    return total


def main():
    with open("input.txt") as in_file:
        return solve_p2(in_file.readlines())


if __name__ == "__main__":
    print(main())
