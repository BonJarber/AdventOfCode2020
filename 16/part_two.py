"""

"""
from functools import reduce
from typing import List


def solve_p2(rules: List[str], tickets: List[str], my_ticket: str):
    ticket_rules = {}
    for rule in rules:
        name = input_ranges = rule.split(":")[0]
        input_ranges = rule.split(":")[1].split(" or ")
        ticket_rules[name] = [
            (int(input_ranges[0].split("-")[0]), int(input_ranges[0].split("-")[1])),
            (int(input_ranges[1].split("-")[0]), int(input_ranges[1].split("-")[1])),
        ]

    valid_tickets = []
    invalids = []
    for ticket in tickets:
        nums = ticket.split(",")
        valid_ticket = True
        for i in range(0, len(nums)):
            valid = False
            for rule in ticket_rules:
                if (
                    ticket_rules[rule][0][0] <= int(nums[i]) <= ticket_rules[rule][0][1]
                    or ticket_rules[rule][1][0]
                    <= int(nums[i])
                    <= ticket_rules[rule][1][1]
                ):
                    valid = True

            if not valid:
                valid_ticket = False
                invalids.append(int(nums[i]))

        if valid_ticket:
            valid_tickets.append(nums)

    valid_names = {}
    invalid_names = {}
    for i in range(0, len(rules)):
        valid_names[i] = set()
        invalid_names[i] = set()
    for ticket in valid_tickets:
        for i in range(0, len(ticket)):
            for rule in ticket_rules:
                if (
                    ticket_rules[rule][0][0]
                    <= int(ticket[i])
                    <= ticket_rules[rule][0][1]
                    or ticket_rules[rule][1][0]
                    <= int(ticket[i])
                    <= ticket_rules[rule][1][1]
                ):
                    if rule not in invalid_names[i]:
                        valid_names[i].add(rule)
                else:
                    invalid_names[i].add(rule)
                    if rule in valid_names[i]:
                        valid_names[i].discard(rule)

    success = False
    while not success:
        finished = True
        for field in valid_names:
            if len(valid_names[field]) == 1:
                val = next(iter(valid_names[field]))
                for field_a in valid_names:
                    if field_a != field:
                        valid_names[field_a].discard(val)
            else:
                finished = False

        if finished:
            success = True

    my_ticket = my_ticket.split(",")
    results = []
    for i in valid_names:
        name = next(iter(valid_names[i]))
        if name.startswith("departure"):
            results.append(int(my_ticket[i]))

    return reduce(lambda x, y: x * y, results)


def main():
    with open("input.txt") as in_file:
        input_fields = in_file.read().split("\n\n")
        return solve_p2(
            input_fields[0].split("\n"),
            input_fields[2].split("\n")[1:],
            input_fields[1].split("\n")[1],
        )


if __name__ == "__main__":
    print(main())
