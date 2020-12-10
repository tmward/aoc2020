#!/usr/bin/env python3
from collections import Counter

with open("input.txt", "r") as ifile:
    nums = [ int(l) for l in ifile]

nums_sorted = [0] + sorted(nums)
# for your adapter that is 3 joules higher
nums_sorted.append(nums_sorted[-1] + 3)

diffs = []
for i, n in enumerate(nums_sorted):
    if i == 0:
        continue
    diffs.append(n - nums_sorted[i - 1])

diffs_counted = Counter(diffs)
print(f"Part 1 solution is {diffs_counted.get(1) * diffs_counted.get(3)}")

# add previous 3 (turns out this is a "tribonacci" sequence)
n1s_to_npaths = [1, 1, 2, 4, 7, 11]

paths = "".join(str(n) for n in diffs).split("3")
num_paths = 1

for path in paths:
    num_paths *= n1s_to_npaths[len(path)]

print(f"Part 2 solution is {num_paths}")
