#!/usr/bin/env python3
from itertools import chain, permutations
from operator import itemgetter
from pprint import pprint
import re
import sys


def parse_rules(raw_rules):
    rule_rgx = re.compile(r"^(\w+\s?\w*):\s+(\d+)\-(\d+)\s+or\s+(\d+)\-(\d+)\s*$")
    field_to_ranges = {}
    for rule in raw_rules.split("\n"):
        if (m := rule_rgx.match(rule)) :
            field = m.group(1)
            min1, max1, min2, max2 = (int(m) for m in m.group(2, 3, 4, 5))
            # inclusive of max1 and max2 so add 1
            field_to_ranges[field] = set(
                chain(range(min1, max1 + 1), range(min2, max2 + 1))
            )
    return field_to_ranges


def parse_ticket(line):
    return [int(n) for n in line.strip().split(",")]


def parse_tickets(block):
    if block.startswith("your"):
        return parse_ticket(block.split("\n")[1])
    return [parse_ticket(line) for line in block.strip().split("\n")[1:]]


def get_input(filename):
    with open(filename, "r") as f:
        rawinput = f.read().split("\n\n")
    return (
        parse_rules(rawinput[0]),
        parse_tickets(rawinput[1]),
        parse_tickets(rawinput[2]),
    )


def valid_ticket(rules, ticket):
    for value in ticket:
        if all(value not in valid_ns for valid_ns in rules.values()):
            return False
    return True


def solve_pt_1(rules, tickets):
    invalid_values = []
    for ticket in tickets:
        for value in ticket:
            if all(value not in valid_ns for valid_ns in rules.values()):
                invalid_values.append(value)
    return sum(invalid_values)


def solve_pt_2(rules, tickets):
    for order_n_rules in permutations(rules.items(), len(rules)):
        next_rule = False
        # order n rules is an ordering of rules of ((field, valid ns),...)
        # pull out valid ns in their order
        rules = tuple(map(itemgetter(1), order_n_rules))
        for ticket in tickets:
            if next_rule:
                break
            for value, valid_nums in zip(ticket, rules): 
                if value not in valid_nums:
                    next_rule = True
                    break
        else:
            return order_n_rules


def main():
    if len(sys.argv) != 2:
        print("Usage: ./solve.py inputfile")
        sys.exit(2)

    rules, ticket, other_tickets = get_input(sys.argv[1])
    print(f"Pt 1 answer: {solve_pt_1(rules, other_tickets)}")
    valid_tickets = [ticket for ticket in other_tickets if valid_ticket(rules, ticket)]
    pprint(solve_pt_2(rules, valid_tickets))


if __name__ == "__main__":
    main()
