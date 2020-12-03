#!/usr/bin/env python3
from functools import partial, reduce
from itertools import compress, count, cycle, islice, starmap
from operator import mul


def get_input(filename):
    with open(filename, "r") as input_file:
        # returning list not a generator because I'll need to go through
        # it several times for part two. Faster to load into memory once
        # and use that copy repeatably then reading from file multiple
        # times
        return [l.strip() for l in input_file]


def terrain(tree_patterns):
    for pattern in tree_patterns:
        yield cycle(pattern)


def levels_to_travel(levels, down_travel):
    # only want to pick the terrain levels (rows) that the sled travels
    # Always pick the first row (so True) then the number of rows to
    # skip is equal to the (down_travel - 1). Repeat this with cycle
    # then to select the terrain travelled with compress
    return compress(levels, cycle([True] + [False] * (down_travel - 1)))


def path(levels, right_travel):
    for level, position in zip(levels, count(0, right_travel)):
        # need next() because islice() returns an iterator even though
        # we are only slicing a single item
        yield next(islice(level, position, position + 1))


def trees(tree_patterns, down_travel, right_travel):
    sled_path = path(
        levels_to_travel(terrain(tree_patterns), down_travel), right_travel
    )
    return sum(point == "#" for point in sled_path)


def main():
    tree_patterns = get_input("input.txt")
    trees_hit = partial(trees, tree_patterns)

    print("Part 1 solution:", trees_hit(1, 3))

    # Part 2 slopes to calculate trees hit (down travel, right travel)
    slopes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    print("Part 2 solution:", reduce(mul, starmap(trees_hit, slopes)))


if __name__ == "__main__":
    main()
