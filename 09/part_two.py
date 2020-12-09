"""

"""
from typing import List


def solve_p2(xmas_code: List[int]):
    window_size = 25
    window = []
    target = None
    for i in range(0, window_size):
        window.append(int(xmas_code[i]))

    for i in range(window_size, len(xmas_code)):
        is_valid = False
        current = xmas_code[i]
        for j in range(0, window_size):
            for k in range(0, window_size):
                if j != k and window[j] + window[k] == current:
                    is_valid = True
        if not is_valid:
            target = current
            break

        window.pop(0)
        window.append(xmas_code[i])

    start = 0
    end = 1
    success = False

    while not success:
        current_sum = sum(xmas_code[start:end])
        if current_sum == target:
            return min(xmas_code[start:end]) + max(xmas_code[start:end])
        elif current_sum < target:
            end += 1
        else:
            start += 1


def main():
    with open("input.txt") as in_file:
        puzzle_input = in_file.readlines()
        int_list = [int(i) for i in puzzle_input]
        return solve_p2(int_list)


if __name__ == "__main__":
    print(main())
