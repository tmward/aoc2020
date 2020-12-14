#!/usr/bin/env python3
import re
import sys


def get_mask(line):
    return re.search(r"[01X]{36}", line).group(0)


def get_mem(line):
    return [int(m) for m in re.search(r"^mem\[(\d+)\]\s+=\s+(\d+)", line).group(1, 2)]


def binary36(value):
    # prepend 0's until its 36 chars wide after converting it to binary
    return f"{value:0=36b}"


def addresses(mask, idx):
    bidx = binary36(idx)
    first_pass_bidx = ""
    # implement the first pass pushing bitmask's 1s and Xs into value
    for m, v in zip(mask, bidx):
        if m == "0":
            first_pass_bidx += v
        else:
            first_pass_bidx += m
    # calculate all the permutations of addresses with floating bits
    locations = [first_pass_bidx]
    while "X" in first_pass_bidx:
        new_locations = []
        for location in locations:
            new_locations.append(location.replace("X", "0", 1))
            new_locations.append(location.replace("X", "1", 1))
        first_pass_bidx = first_pass_bidx.replace("X", "0", 1)
        locations = new_locations.copy()
    return (int(l, 2) for l in locations)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: ./solve_pt2.py inputfile")
        sys.exit(2)

    mem = {}
    with open(sys.argv[1], "r") as ifile:
        for l in ifile:
            if l.startswith("mask"):
                mask = get_mask(l)
            elif l.startswith("mem"):
                idx, value = get_mem(l)
                for a in addresses(mask, idx):
                    mem[a] = value
    print(f"Pt 2 answer: {sum(mem.values())}")


if __name__ == "__main__":
    main()
