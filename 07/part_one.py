"""

"""
import re
from typing import List


class Bag:
    def __init__(self, color: str, rules: str) -> None:
        self.color = color
        self.contains = {}
        if "no other bags" not in rules:
            for rule in rules.split(","):
                color, count = self.parse_rule(rule)
                self.contains[color] = int(count)

    def parse_rule(self, rule: str):
        BAG_RULE_REGEX = ".*?(\d+) ([a-z]+? [a-z]+?) bag"
        m = re.match(BAG_RULE_REGEX, rule)
        if not m:
            Exception("Something went wrong with the regex")
        else:
            return m.group(2), m.group(1)


def solve_p1(all_rules: List[str]):
    available_bags = {}
    my_bag = "shiny gold"
    total_count = 0

    def can_hold_my_bag(bag_to_check: Bag) -> bool:
        can_hold = False
        for color in bag_to_check.contains.keys():
            if color == my_bag:
                can_hold = True
            if can_hold_my_bag(available_bags[color]):
                can_hold = True

        return can_hold

    for rule in all_rules:
        RULE_REGEX = "([a-z]+ [a-z]+) bags contain (.+)\.$"
        m = re.match(RULE_REGEX, rule.strip())
        bag = Bag(m.group(1), m.group(2))
        available_bags[bag.color] = bag

    for bag in available_bags.values():
        if can_hold_my_bag(bag):
            total_count += 1

    return total_count


def main():
    with open("input.txt") as in_file:
        return solve_p1(in_file.readlines())


if __name__ == "__main__":
    print(main())
