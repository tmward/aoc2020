#!/usr/bin/env python3
import re
import sys


def get_mask(line):
    return re.search(r"[01X]{36}", line).group(0)


def get_mem(line):
    return [int(m) for m in re.search(r"^mem\[(\d+)\]\s+=\s+(\d+)", line).group(1, 2)]


def binary36(value):
    # prepend 36 0 digits to value and convert it to binary
    return f"{value:0=36b}"


def result(mask, value):
    bvalue = binary36(value)
    r = ""
    for m, v in zip(mask, bvalue):
        if m == "X":
            r += v
        else:
            r += m
    return int(r, 2)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: ./solve.py inputfile")
        sys.exit(2)

    mem = {}
    with open(sys.argv[1], "r") as ifile:
        for l in ifile:
            if l.startswith("mask"):
                mask = get_mask(l)
            elif l.startswith("mem"):
                idx, value = get_mem(l)
                mem[idx] = result(mask, value)
    print(f"Pt 1 answer: {sum(mem.values())}")


if __name__ == "__main__":
    main()
