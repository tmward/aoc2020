#!/usr/bin/env python3
from itertools import combinations
from functools import reduce
from operator import mul

with open('input.txt', 'r') as ifile:
    nums = {int(n) for n in ifile}

print("Part 1's answer:")
for a, b in combinations(nums, 2):
    if a + b == 2020:
        print(a * b)
        break

print("Part 2's answer:")
for combo in combinations(nums, 3):
    if sum(combo) == 2020:
        print(reduce(mul, combo))
        break
