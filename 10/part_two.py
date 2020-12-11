"""

"""
import copy
from typing import List, Set

TOTAL_SOLUTIONS = 0


def solve_p2(adapter_list: List[int]):
    built_in_adapter = max(adapter_list) + 3
    adapter_set = set(i for i in adapter_list)
    adapter_set.add(built_in_adapter)
    seen_variations = set()
    additional_variations = []

    def compute_variation(
        current_adapter_set: Set[int], current_adapter=0, current_variation=""
    ):
        while current_adapter_set != set():
            solved = False
            new_adapter = None
            new_variation = None
            for i in range(1, 4):
                if current_adapter + i in current_adapter_set:
                    if not new_adapter:
                        new_adapter = current_adapter + i
                        new_variation = current_variation + f", {new_adapter}"
                        current_adapter_set.discard(new_adapter)
                    else:
                        additional_variations.append(
                            [
                                current_adapter_set.copy(),
                                current_adapter,
                                current_variation,
                            ]
                        )

            current_adapter = new_adapter
            current_variation = new_variation
            if not current_adapter:
                return False

        if current_variation not in seen_variations:
            seen_variations.add(current_variation)

        return True

    additional_variations.append([adapter_set, 0, ""])
    while additional_variations != []:
        current = additional_variations.pop(0)
        compute_variation(current[0], current[1], current[2])
    return len(seen_variations)


def main():
    with open("input.txt") as in_file:
        puzzle_input = in_file.readlines()
        int_list = [int(i) for i in puzzle_input]
        return solve_p2(int_list)


if __name__ == "__main__":
    print(main())
