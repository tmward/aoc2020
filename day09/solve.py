#!/usr/bin/env python3
from collections import deque
from itertools import combinations

with open("input.txt", "r") as ifile:
    ns = [int(l) for l in ifile]

prev_ns = deque(ns[:25])

for n in ns[25:]:
    if all(num1 + num2 != n for num1, num2 in combinations(prev_ns, 2)):
        print(f"Part 1 solution: {n}")
    prev_ns.popleft()
    prev_ns.append(n)
