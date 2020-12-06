#!/usr/bin/env python3
from collections import Counter
from string import whitespace

def filter_whitespace(response):
    return [r for r in response if r not in whitespace]

with open("input.txt", "r") as ifile:
    responses = [
        filter_whitespace(response)
        for response in ifile.read().split("\n\n")
    ]

print("Part 1 answer")
print(sum(len(Counter(r)) for r in responses))
