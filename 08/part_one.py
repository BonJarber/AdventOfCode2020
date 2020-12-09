"""

"""
from typing import List


def solve_p1(instructions: List[str]):
    accumulator = 0
    seen = set()
    pointer = 0
    termination = len(instructions)
    while True:
        if pointer == termination:
            return accumulator
        if pointer in seen:
            return accumulator
        else:
            seen.add(pointer)

        command, value = instructions[pointer].strip().split(" ")
        if command == "nop":
            pointer += 1
            continue
        elif command == "acc":
            accumulator += int(value)
            pointer += 1
            continue
        elif command == "jmp":
            pointer += int(value)


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
