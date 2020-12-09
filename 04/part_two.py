"""
Count the number of valid passports - those that have all required fields. 
Treat cid as optional. In your batch file, how many passports are valid?
"""
import re
from typing import List

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def solve_p2(passport_batch: List[str]):
    count = 0
    current_check = REQUIRED_FIELDS.copy()
    for line in passport_batch:
        if line == "\n":
            if len(current_check) == 0:
                count += 1
            current_check = REQUIRED_FIELDS.copy()
        fields = line.split(" ")
        for key_value in fields:
            is_valid = False
            if key_value != "\n":
                key, value = key_value.split(":")
                value = value.strip()
                if key == "byr":
                    if int(value) >= 1920 and int(value) <= 2002:
                        is_valid = True
                elif key == "iyr":
                    if int(value) >= 2010 and int(value) <= 2020:
                        is_valid = True
                elif key == "eyr":
                    if int(value) >= 2020 and int(value) <= 2030:
                        is_valid = True
                elif key == "hgt":
                    hgt_regex = "^(\d+)([incm]{2})$"
                    m = re.match(hgt_regex, value)
                    if m and len(m.groups()) == 2:
                        if m.group(2) == "in":
                            if int(m.group(1)) >= 59 and int(m.group(1)) <= 76:
                                is_valid = True
                        elif m.group(2) == "cm":
                            if int(m.group(1)) >= 150 and int(m.group(1)) <= 193:
                                is_valid = True
                elif key == "hcl":
                    hcl_regex = "^#[a-f0-9]{6}$"
                    m = re.match(hcl_regex, value)
                    if m:
                        is_valid = True
                elif key == "ecl":
                    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    if value in valid_ecl:
                        is_valid = True
                elif key == "pid":
                    pid_regex = "^\d{9}$"
                    m = re.match(pid_regex, value)
                    if m:
                        is_valid = True

                if is_valid:
                    current_check.remove(key)

    if len(current_check) == 0:
        count += 1
    return f"{count} passports"


def main():
    with open("input.txt") as in_file:
        return solve_p2(in_file.readlines())


if __name__ == "__main__":
    print(main())
