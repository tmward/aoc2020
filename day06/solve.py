#!/usr/bin/env python3
from collections import Counter
from functools import reduce
from operator import add
from string import whitespace


def filter_whitespace(response):
    return [r for r in response if r not in whitespace]


with open("input.txt", "r") as ifile:
    responses = [filter_whitespace(response) for response in ifile.read().split("\n\n")]

print("Part 1 answer")
print(sum(len(Counter(r)) for r in responses))


print("Part 2 answer")
# Going to have to take a much different approach than pt 1
with open("input.txt", "r") as ifile:
    forms = [
        [Counter(response) for response in responses.splitlines()]
        for responses in ifile.read().split("\n\n")
    ]

# Logic behind this: each f in forms is a list of a Counter for each
# person in the groups response. The Counter's elements are just the
# letter = 1 if that person responded. By adding all the Counters for a
# single group up, if each person responded yes to a single answer, then
# the count for that letter should be the same as the number of people
# in the group (i.e. the length of that group). Sum all that up.
print(sum(sum(v == len(f) for v in reduce(add, f).values()) for f in forms))
