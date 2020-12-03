#!/usr/bin/env python3
import re

# lines formatted min-max letter: password
pattern = re.compile(r"^\s*(\d+)\-(\d+)\s+([a-zA-Z]):\s+([a-zA-Z]+)\s*$")

with open("input.txt", "r") as lines:
    passwords = [m.groups() for l in lines if (m := pattern.search(l)) is not None]

print(
    "Part 1 solution:",
    len([p for p in passwords if int(p[0]) <= p[3].count(p[2]) <= int(p[1])])
)

print(
    "Part 2 solution pt 2",
    sum((p[int(a) - 1] == l) ^ (p[int(b) - 1] == l) for a, b, l, p in passwords)
)
