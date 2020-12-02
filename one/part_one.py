"""
Find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

"""


def main():
    with open("input.txt") as in_file:
        values = set()
        for line in in_file:
            curr = int(line)
            values.add(curr)
            inverse = 2020 - curr
            if inverse in values:
                return f"Success! The numbers were {inverse} and {curr}. The solution is {inverse * curr}"
            else:
                values.add(inverse)

    return "No solution found"


if __name__ == "__main__":
    print(main())
