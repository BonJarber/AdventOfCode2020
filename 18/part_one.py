"""

"""
from typing import List


def perform_action(total, new, operator):
    if operator == "+":
        total += new
    elif operator == "-":
        total -= new
    else:
        total = total * new

    return total


def sum_chars(line: str):
    # print("Starting new sum_chars")
    curr_total = None
    curr_operator = None
    operators = {"+", "-", "*"}
    ints = {i for i in range(0, 10)}
    i = 0
    while i < len(line):
        if line[i] != " ":
            pass
            # print(f"Checking {line[i]} at place [{i}]")
        if line[i] == " ":
            i += 1
            continue
        elif line[i] == ")" or line[i] == "\n":
            # print(f"Returning {curr_total} and i = {i}")
            return curr_total, i + 1
        elif line[i] in operators:
            curr_operator = line[i]
        elif line[i] == "(":
            result = sum_chars(line[i + 1 :])
            i += result[1]
            if curr_total is None:
                curr_total = result[0]
            else:
                curr_total = perform_action(curr_total, result[0], curr_operator)
        elif int(line[i]) in ints:
            if curr_total is None:
                curr_total = int(line[i])
            else:
                curr_total = perform_action(curr_total, int(line[i]), curr_operator)

        i += 1
        # print(f"Current total: {curr_total}")
    # print(f"Returning {curr_total} and i = {i}")
    return curr_total, len(line) - 1


def solve_p1(homework: List[str]):
    results = []
    for line in homework:
        result = sum_chars(line)
        results.append(result[0])
        # print(result[0])
    return sum(results)


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
