"""

"""
from typing import List


def solve_p1(rules: List[str], tickets: List[str]):
    ranges = []
    for rule in rules:
        input_ranges = rule.split(':')[1].split(' or ')
        ranges.append((int(input_ranges[0].split('-')[0]), int(input_ranges[0].split('-')[1])))
        ranges.append((int(input_ranges[1].split('-')[0]), int(input_ranges[1].split('-')[1])))
    
    invalids = []
    for ticket in tickets:
        nums = ticket.split(',')
        for num in nums:
            valid = False
            for low, high in ranges:
                if low <= int(num) <= high:
                    valid = True
            
            if not valid:
                invalids.append(int(num))
    
    return sum(invalids)


def main():
    with open("input.txt") as in_file:
        input_fields = in_file.read().split('\n\n')
        return solve_p1(input_fields[0].split('\n'), input_fields[2].split('\n')[1:])


if __name__ == "__main__":
    print(main())
