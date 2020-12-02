"""
To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""
import re
from typing import List


def solve_p1(passwords: List[str]):
    total_valid = 0
    parse_password_regex = "(\d+)-(\d+) ([a-z]): ([a-z]+)"
    for password_rule in passwords:
        m = re.match(parse_password_regex, password_rule)
        min_val = m.group(1)
        max_val = m.group(2)
        letter = m.group(3)
        password = m.group(4)
        password_regex = (
            f"^[^{letter}]*({letter}[^{letter}]*?){{{min_val},{max_val}}}[^{letter}]*$"
        )
        is_valid = re.match(password_regex, password)
        if is_valid:
            total_valid += 1

    return total_valid


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
