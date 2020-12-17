#!/usr/bin/env python3
"""Day 17 for advent of code solution"""
from collections import defaultdict
from copy import deepcopy
from itertools import chain, product
import sys


def get_input(filename):
    # credit to TDM for this terror
    z_to_coords = defaultdict(lambda: defaultdict(lambda: "."))
    with open(filename, "r") as f:
        # return dict with one key, 0 (for z = 0), and x, y coordinates
        # flattened into complex numbers pointing to their values
        for r, line in enumerate(f):
            for c, val in enumerate(line.strip()):
                z_to_coords[0][complex(c, r)] = val
    return z_to_coords


def print_plane(coords):
    reals = {int(n.real) for n in coords}
    imags = {int(n.imag) for n in coords}
    for y in range(min(imags), max(imags) + 1):
        row = []
        for x in range(min(reals), max(reals) + 1):
            row.append(coords[complex(x, y)])
        print(*row, sep = "")


def print_planes(z_to_coords, iteration):
    print(f"After {iteration} iteration(s):")
    for z in sorted(z_to_coords):
        print(f"z = {z}")
        print_plane(z_to_coords[z])


def neighboring_coords(z, coord):
    for delta_z in (-1, 0, 1):
        for increment in product((-1, 0, 1), repeat=2):
            neighbor = coord + complex(*increment)
            # don't yield itself as a "neighbor" (aka when delta_z = 0)
            if not (neighbor == coord and delta_z == 0):
                yield z + delta_z, neighbor


def get_state(z_to_coords, z, coord):
    # return empty ('.') if no known state in that area
    # do not rely on defaultdict behavior since that will then
    # initialize that value and lead to modification of the
    # datastructure
    return z_to_coords.get(z, {}).get(coord, ".")


def active(z_to_coords, z, coord):
    return get_state(z_to_coords, z, coord) == "#"


def total_active(z_to_coords):
    return sum(
        state == "#"
        for coord_to_state in z_to_coords.values()
        for state in coord_to_state.values()
    )


def expand_grid(z_to_coords):
    # this is janky... but since we have nested defaultdicts, if a point
    # is accessed it'll become "empty". So find all the neighbors of the
    # current points then check the contents of all the neighbors (and
    # not do anything with it)
    neighbors = set()
    for z in z_to_coords:
        # coords are same for each z, so just check z = 0
        for coord in z_to_coords[0]:
            for neighbor in neighboring_coords(z, coord):
                neighbors.add(neighbor)
    for z, coord in neighbors:
        # abuses defaultdict, woo!
        z_to_coords[z][coord]


def solve_pt_1(z_to_coords):
    for _ in range(1, 7):
        expand_grid(z_to_coords)
        new_z_to_coords = deepcopy(z_to_coords)
        for z, coord_to_state in z_to_coords.items():
            for coord, state in coord_to_state.items():
                active_neighbors = sum(
                    active(z_to_coords, n_z, n_coord) for n_z, n_coord in neighboring_coords(z, coord)
                )
                if state == "." and active_neighbors == 3:
                    new_z_to_coords[z][coord] = "#"
                elif state == "#" and active_neighbors not in (2, 3):
                    new_z_to_coords[z][coord] = "."
        z_to_coords = deepcopy(new_z_to_coords)
    return total_active(z_to_coords)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} inputfile")
        sys.exit(2)
    print(f"Pt 1 solution: {solve_pt_1(get_input(sys.argv[1]))}")


if __name__ == "__main__":
    main()
