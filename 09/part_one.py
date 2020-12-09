"""

"""
from typing import List


def solve_p1(xmas_code: List[str]):
    window_size = 25
    window = []
    for i in range(0, window_size):
        window.append(int(xmas_code[i]))

    for i in range(window_size, len(xmas_code)):
        is_valid = False
        current = int(xmas_code[i])
        for j in range(0, window_size):
            for k in range(0, window_size):
                if j != k and int(window[j]) + int(window[k]) == current:
                    is_valid = True
        if not is_valid:
            return current

        window.pop(0)
        window.append(xmas_code[i])


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
