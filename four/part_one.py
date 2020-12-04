"""
Count the number of valid passports - those that have all required fields. 
Treat cid as optional. In your batch file, how many passports are valid?
"""
from typing import List

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def solve_p1(passport_batch: List[str]):
    count = 0
    current_check = REQUIRED_FIELDS.copy()
    for line in passport_batch:
        if line == "\n":
            if len(current_check) == 0:
                count += 1
            current_check = REQUIRED_FIELDS.copy()
        fields = line.split(" ")
        for field in fields:
            if field != "\n":
                value = field.split(":")[0]
                if value != "cid":
                    current_check.remove(field.split(":")[0])

    return f"{count} passports"


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
