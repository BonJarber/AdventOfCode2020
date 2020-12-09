"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
"""
import re
from typing import List


def solve_p2(passwords: List[str]):
    total_valid = 0
    parse_password_regex = "(\d+)-(\d+) ([a-z]): ([a-z]+)"
    for password_rule in passwords:
        m = re.match(parse_password_regex, password_rule)
        index_1 = int(m.group(1))
        index_2 = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        letter_appears = False

        if len(password) >= index_1:
            if password[index_1 - 1] == letter:
                letter_appears = True
        if len(password) >= index_2:
            if password[index_2 - 1] == letter:
                if letter_appears:
                    continue
                else:
                    letter_appears = True
        if letter_appears:
            total_valid += 1

    return total_valid


def main():
    with open("input.txt") as in_file:
        return solve_p2(in_file.readlines())


if __name__ == "__main__":
    print(main())
