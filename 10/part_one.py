"""

"""
from typing import List


def solve_p1(adapter_list: List[int]):
    built_in_adapter = max(adapter_list) + 3
    adapter_set = set(i for i in adapter_list)
    adapter_set.add(built_in_adapter)
    current_adapter = 0
    one_jolts = 0
    three_jolts = 0

    while adapter_set != set():
        for i in range(1, 4):
            if current_adapter + i in adapter_set:
                current_adapter = current_adapter + i
                adapter_set.discard(current_adapter)
                if i == 1:
                    one_jolts += 1
                elif i == 3:
                    three_jolts += 1
                break

    return one_jolts, three_jolts, one_jolts * three_jolts


def main():
    with open("input.txt") as in_file:
        puzzle_input = in_file.readlines()
        int_list = [int(i) for i in puzzle_input]
        return solve_p1(int_list)


if __name__ == "__main__":
    print(main())
