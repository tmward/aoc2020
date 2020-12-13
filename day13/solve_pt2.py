#!/usr/bin/env python3
from itertools import count
import sys


def get_input(filename):
    with open(filename, "r") as ifile:
        return [
            int(t) if t != "x" else 1 for t in ifile.read().splitlines()[1].split(",")
        ]


def solve(buses):
    n = 1
    step = 1
    for i, b in enumerate(buses):
        n = next(c for c in count(n, step) if (c + i) % b == 0)
        step *= b
    return n


def main():
    if len(sys.argv) != 2:
        print("Usage: ./solve_pt2.py inputfile")
        sys.exit(2)
    print(f"Part 2 solution: {solve(get_input(sys.argv[1]))}")


if __name__ == "__main__":
    main()
