#!/usr/bin/env python3
from itertools import count, cycle, islice
from pprint import pprint

with open("input.txt", "r") as ifile:
    print("Part 1 solution:")
    print(
        # use True == 1 and False == 0 to our advantage
        sum(
            # check if it's a tree
            map(
                lambda x: x == "#",
                # need to use next to get the actual value since islice
                # returns an iterator
                map(
                    next,
                    # pull the correct spot the sled goes through on
                    # each line
                    map(
                        islice,
                        # get the lines and make them repeat forever
                        map(cycle, map(lambda l: l.strip(), ifile)),
                        count(0, 3),
                        count(1, 3),
                    ),
                ),
            )
        )
    )
