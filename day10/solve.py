#!/usr/bin/env python3
from collections import Counter


with open("input.txt", "r") as ifile:
    nums = [ int(l) for l in ifile]

nums_sorted = sorted(nums)
# for your adapter that is 3 joules higher
nums_sorted.append(nums_sorted[-1] + 3)

diffs = []
for i, n in enumerate(nums_sorted):
    if i == 0:
        diffs.append(n)
    else:
        diffs.append(n - nums_sorted[i - 1])

diffs_counted = Counter(diffs)
print(f"Part 1 solution is {diffs_counted.get(1) * diffs_counted.get(3)}")
#print(f"Part 1 solution is {cum_diff}")
