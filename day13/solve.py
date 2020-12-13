#!/usr/bin/env python3
from itertools import count
import sys


def get_input(filename):
    with open(filename, "r") as ifile:
        raw = ifile.read().splitlines()
    start = int(raw[0])
    buses = [int(t) for t in raw[1].split(",") if t != "x"]
    return start, buses


def solve_pt_one(start, buses):
    for i in count(start):
        for bus in buses:
            if i % bus == 0:
                return bus * (i - start)


def main():
    if len(sys.argv) != 2:
        print("Usage: ./solve.py inputfile")
        sys.exit(2)
    start, buses = get_input(sys.argv[1])
    print(f"Part 1 solution: {solve_pt_one(start, buses)}")


if __name__ == "__main__":
    main()
