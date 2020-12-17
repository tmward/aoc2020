#!/usr/bin/env python3
"""Day 17 for advent of code solution"""
from itertools import product
import sys


def get_input(filename):
    with open(filename, "r") as f:
        actives = set()
        for y, line in enumerate(f):
            for x, val in enumerate(line.strip()):
                if val == "#":
                    actives.add((x, y, 0, 0))
    return actives


def neighbors(x, y, z, w):
    ns = set()
    for dx, dy, dz, dw in product([-1, 0, 1], repeat=4):
        ns.add((dx + x, dy + y, dz + z, dw + w))
    ns.remove((x, y, z, w))
    return ns


def find_ranges(actives):
    xs = set()
    ys = set()
    zs = set()
    ws = set()
    for x, y, z, w in actives:
        xs.add(x)
        ys.add(y)
        zs.add(z)
        ws.add(w)
    return min(xs), max(xs), min(ys), max(ys), min(zs), max(zs), min(ws), max(ws)


def solve_pt_2(actives):
    for _ in range(1, 7):
        minx, maxx, miny, maxy, minz, maxz, minw, maxw = find_ranges(actives)
        new_actives = set()
        for w in range(minw - 1, maxw + 2):
            for z in range(minz - 1, maxz + 2):
                for y in range(miny - 1, maxy + 2):
                    for x in range(minx - 1, maxx + 2):
                        coord = (x, y, z, w)
                        num_active_neighbors = len(actives & neighbors(*coord))
                        if coord in actives and num_active_neighbors in (2, 3):
                            new_actives.add(coord)
                        elif coord not in actives and num_active_neighbors == 3:
                            new_actives.add(coord)
        actives = new_actives
    return len(actives)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} inputfile")
        sys.exit(2)
    print(f"Pt 2 solution: {solve_pt_2(get_input(sys.argv[1]))}")


if __name__ == "__main__":
    main()
