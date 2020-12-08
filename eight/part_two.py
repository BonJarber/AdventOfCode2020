"""

"""
from typing import List


def solve_p2(instructions: List[str]):
    accumulator = 0
    seen = set()
    nop_jmps = []
    fix_pos = -1
    termination = len(instructions)

    pointer = 0
    while True:
        if pointer == termination:
            return f"Program terminated! Value is:\n\n{accumulator}"
        if pointer not in seen:
            seen.add(pointer)
        else:
            fix_pos = nop_jmps.pop(0)[1]
            accumulator = 0
            seen = set()
            pointer = 0

        command, value = instructions[pointer].strip().split(" ")
        if command == "nop":
            if pointer == fix_pos:
                pointer += int(value)
            else:
                nop_jmps.append(("nop", pointer))
                pointer += 1
        elif command == "acc":
            accumulator += int(value)
            pointer += 1
        elif command == "jmp":
            if pointer == fix_pos:
                pointer += 1
            else:
                nop_jmps.append(("nop", pointer))
                pointer += int(value)


def main():
    with open("input.txt") as in_file:
        return solve_p2(in_file.readlines())


if __name__ == "__main__":
    print(main())
