#!/usr/bin/env python3
from itertools import count
import sys


def get_input(filename):
    with open(filename, "r") as ifile:
        return [
            int(t) if t != "x" else 1 for t in ifile.read().splitlines()[1].split(",")
        ]


def solve(buses):
    step = max(buses)
    start = max(buses) * 200000000000
    for t in count(start, step):
        for offset, bus in enumerate(buses):
            if (t + offset) % bus != 0:
                break
        else:
            return t


def main():
    if len(sys.argv) != 2:
        print("Usage: ./solve_pt2.py inputfile")
        sys.exit(2)
    print(f"Part 2 solution: {solve(get_input(sys.argv[1]))}")


if __name__ == "__main__":
    main()
