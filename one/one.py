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
    values = []
    with open("input.txt") as in_file:
        for line in in_file:
            curr = int(line)
            if values == []:
                values.append(curr)
            else:
                for i in values:
                    if i + curr == 2020:
                        return f"Success! The numbers were {i} and {curr}. The solution is {i * curr}"
                values.append(curr)

    return "No solution found"


if __name__ == "__main__":
    print(main())
