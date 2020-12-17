#!/usr/bin/env python3
"""Day 17 for advent of code solution"""
from collections import defaultdict
from copy import deepcopy
from itertools import product
import sys


def get_input(filename):
    z_to_coords = defaultdict(dict)
    with open(filename, "r") as f:
        # return dict with one key, 0 (for z = 0), and x, y coordinates
        # flattened into complex numbers pointing to their values
        z_to_coords[0] = {
            complex(c, r): val
            for r, line in enumerate(f)
            for c, val in enumerate(line.strip())
        }
    return z_to_coords


def print_plane(coords):
    reals = {int(n.real) for n in coords}
    imags = {int(n.imag) for n in coords}
    for y in range(min(imags), max(imags) + 1):
        row = []
        for x in range(min(reals), max(reals) + 1):
            row.append(coords[complex(x, y)])
        print(*row)


def print_planes(z_to_coords, iteration):
    print(f"After {iteration} iteration(s):")
    for z, coord_to_state in z_to_coords.items():
        print(f"z = {z}")
        print_plane(coord_to_state)


def neighboring_coords(z, coord):
    for delta_z in (-1, 0, 1):
        for increment in product((-1, 0, 1), repeat=2):
            neighbor = coord + complex(*increment)
            # don't yield itself as a "neighbor" (aka when delta_z = 0)
            if not (neighbor == coord and delta_z == 0):
                yield z + delta_z, neighbor


def get_state(z_to_coords, z, coord):
    # return empty ('.') if no known state in that area
    return z_to_coords[z].get(coord, ".")


def active(z_to_coords, z, coord):
    # return empty ('.') if no known state in that area
    return get_state(z_to_coords, z, coord) == "#"


def total_active(z_to_coords):
    return sum(
        state == "#"
        for coord_to_state in z_to_coords.values()
        for state in coord_to_state.values()
    )


def solve_pt_1(z_to_coords):
    new_z_to_coords = deepcopy(z_to_coords)
    print_planes(z_to_coords, 0)
    # TODO: add plane above and below before each cycle
    for _ in range(1, 7):
        if _ > 1:
            break
        for z, coord_to_state in z_to_coords.items():
            for coord, state in coord_to_state.items():
                active_neighbors = sum(
                    active(z_to_coords, n_z, n_coord) for n_z, n_coord in neighboring_coords(z, coord)
                )
                if state == "." and active_neighbors == 3:
                    new_z_to_coords[z][coord] = "#"
                elif state == "#" and active_neighbors not in (2, 3):
                    new_z_to_coords[z][coord] = "."
            print("here?")
        z_to_coords = deepcopy(new_z_to_coords)
        print_planes(z_to_coords, _)
    return total_active(z_to_coords)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} inputfile")
        sys.exit(2)
    print(f"Pt 1 solution: {solve_pt_1(get_input(sys.argv[1]))}")


if __name__ == "__main__":
    main()
