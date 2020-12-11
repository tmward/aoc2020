#!/usr/bin/env python3
from collections import Counter
from copy import deepcopy
from itertools import chain, repeat
import sys


def get_layout(filename):
    # adding floors lets us not worry about literal edge cases
    with open(filename, "r") as ifile:
        # add floor around each edge
        layout = [["."] + [c for c in l.strip()] + ["."] for l in ifile]
    # add floor at top and bottom of seats
    blank_row = ["."] * len(layout[0])
    layout.insert(0, blank_row)
    layout.append(blank_row)
    return layout


def adjacent_seats(layout, r, c):
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


def iterate_part_one(layout):
    new_layout = deepcopy(layout)
    for row_num, row in enumerate(layout):
        for col_num, seat in enumerate(row):
            if seat == "L" and all(adjacent_empty(layout, row_num, col_num)):
                new_layout[row_num][col_num] = "#"
            elif seat == "#" and sum(adjacent_occupied(layout, row_num, col_num)) >= 4:
                new_layout[row_num][col_num] = "L"

    return new_layout


def indexes(direction, r, c, nrows, ncols):
    return {
        "n": zip(range(r - 1, -1, -1), repeat(c)),
        "s": zip(range(r + 1, nrows), repeat(c)),
        "w": zip(repeat(r), range(c - 1, -1, -1)),
        "e": zip(repeat(r), range(c + 1, ncols)),
        "nw": zip(range(r - 1, -1, -1), range(c - 1, -1, -1)),
        "ne": zip(range(r - 1, -1, -1), range(c + 1, ncols)),
        "sw": zip(range(r + 1, nrows), range(c - 1, -1, -1)),
        "se": zip(range(r + 1, nrows), range(c + 1, ncols)),
    }.get(direction)


def first_visible_seats(layout, r, c):
    directions = ["n", "s", "e", "w", "ne", "nw", "sw", "se"]
    nrows = len(layout)
    ncols = len(layout[r])
    visible_seats = []
    for direction in directions:
        for i, j in indexes(direction, r, c, nrows, ncols):
            if (seat := layout[i][j]) in ("L", "#"):
                visible_seats.append(seat)
                break
    return Counter(visible_seats)


def no_visible_occupied(layout, r, c):
    return first_visible_seats(layout, r, c)["#"] == 0


def gets_vacated(layout, r, c):
    return first_visible_seats(layout, r, c)["#"] >= 5


def iterate_part_two(layout):
    new_layout = deepcopy(layout)
    for row_num, row in enumerate(layout):
        for col_num, seat in enumerate(row):
            if seat == "L" and no_visible_occupied(layout, row_num, col_num):
                new_layout[row_num][col_num] = "#"
            elif seat == "#" and gets_vacated(layout, row_num, col_num):
                new_layout[row_num][col_num] = "L"

    return new_layout


def occupied_seats(layout):
    return sum(s == "#" for s in chain.from_iterable(layout))


def solve(layout, iterate_func):
    while True:
        n_occupied = occupied_seats(layout)
        layout = iterate_func(layout)
        if n_occupied == occupied_seats(layout):
            return n_occupied


def main():
    if len(sys.argv) != 2:
        print("Usage: ./solve.py inputfile")
        sys.exit(2)
    layout = get_layout(sys.argv[1])
    print(f"Part 1 answer: {solve(layout, iterate_part_one)}")
    print(f"Part 2 answer: {solve(layout, iterate_part_two)}")


if __name__ == "__main__":
    main()
