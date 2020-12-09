#!/usr/bin/env python3
from collections import deque
from itertools import combinations
from sys import exit

with open("input.txt", "r") as ifile:
    ns = [int(l) for l in ifile]

prev_ns = deque(ns[:25])

for n in ns[25:]:
    if all(num1 + num2 != n for num1, num2 in combinations(prev_ns, 2)):
        weakness = n
        break
    prev_ns.popleft()
    prev_ns.append(n)

print(f"Part 1 solution: {weakness}")

# Pt 2 solution
# algorithm: brute force by obtaining all the possible subslices
for i in range(len(ns) - 1):
    seq = ns[i:]
    for a in range(2, len(seq)):
        run = seq[:a]
        if sum(run) == weakness:
            print(f"Part 2 solution: {min(run) + max(run)}")
            exit()
