"""
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
"""
from typing import List


def solve_p2(numbers: List[int]):
    previous_input = None
    current_input = None
    sums = {}
    numbers.sort()
    for line in numbers:
        if previous_input is None:
            previous_input = int(line)
            continue
        current_input = int(line)
        inverse = 2020 - current_input
        if inverse in sums.keys():
            return f"The values were {current_input}, {sums[inverse][0]}, {sums[inverse][1]}. The solution is:\n {current_input*sums[inverse][0]*sums[inverse][1]}"
        else:
            current_sum = current_input + previous_input
            sums[current_sum] = (current_input, previous_input)
            previous_input = current_input

    return "No solution found"


def main():
    with open("input.txt") as in_file:
        return solve_p2(in_file.readlines())


if __name__ == "__main__":
    print(main())
