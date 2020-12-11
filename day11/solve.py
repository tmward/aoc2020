#!/usr/bin/env python3
from copy import deepcopy
from itertools import chain
from pprint import pprint
import sys


def get_layout(filename):
    with open(filename, "r") as ifile:
        # add floor around each edge
        layout = [["."] + [c for c in l.strip()] + ["."] for l in ifile]

    # add floor at top and bottom of seats
    blank_row = ["."] * len(layout[0])
    layout.insert(0, blank_row)
    layout.append(blank_row)
    return layout


def adjacent_seats(layout, r, c):
    # TODO replace with chain?
    return (
        layout[r - 1][c - 1 : c + 2]
        + [layout[r][c - 1]]
        + [layout[r][c + 1]]
        + layout[r + 1][c - 1 : c + 2]
    )


def adjacent_occupied(layout, r, c):
    return [s == "#" for s in adjacent_seats(layout, r, c)]


def adjacent_empty(layout, r, c):
    return [s in (".", "L") for s in adjacent_seats(layout, r, c)]


def iterate(layout):
    new_layout = deepcopy(layout)
    for row_num, row in enumerate(layout):
        for col_num, seat in enumerate(row):
            if seat == ".":
                continue
            elif seat == "L" and all(adjacent_empty(layout, row_num, col_num)):
                new_layout[row_num][col_num] = "#"
            elif seat == "#" and sum(adjacent_occupied(layout, row_num, col_num)) >= 4:
                new_layout[row_num][col_num] = "L"

    return new_layout


def occupied_seats(layout):
    return sum(s == "#" for s in chain.from_iterable(layout))


def main():
    layout = get_layout(sys.argv[1])
    while True:
        n_occupied = occupied_seats(layout)
        layout = iterate(layout)
        if n_occupied == occupied_seats(layout):
            print(f"Part 1 answer: {n_occupied}")
            sys.exit()


if __name__ == "__main__":
    main()
