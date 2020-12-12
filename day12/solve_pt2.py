#!/usr/bin/env python3
from math import cos, radians, sin
import re
import sys


def fix_type(d, a):
    return (d, int(a))


def get_input(filename):
    rgx = re.compile(r"([A-Z]+)(\d+)")
    with open(filename, "r") as ifile:
        return [fix_type(*m.groups()) for l in ifile if (m := rgx.match(l))]


def round_complex(cnum):
    return complex(round(cnum.real), round(cnum.imag))


def rotate(coord, direction, degree):
    if direction == "R":
        degree *= -1
    rads = radians(degree)
    # floating point arithmetic issues, so round to fix them
    return round_complex(coord * complex(cos(rads), sin(rads)))


def advance(coord, direction, amount):
    d_to_i = {
        "E": complex(1),
        "N": complex(0, 1),
        "W": complex(-1),
        "S": complex(0, -1),
    }
    return coord + d_to_i.get(direction) * amount


def follow(d_and_as):
    coord = complex(0, 0)
    waypoint = complex(10, 1)
    for d, a in d_and_as:
        if d in ("R", "L"):
            waypoint = rotate(waypoint, d, a)
        elif d == "F":
            coord += waypoint * a
        else:
            waypoint = advance(waypoint, d, a)
    return coord


def main():
    if len(sys.argv) != 2:
        print("usage: ./solve.py inputfile")
        sys.exit(2)
    d_and_as = get_input(sys.argv[1])
    final_coord = follow(d_and_as)
    print(f"Part 2 answer: {abs(final_coord.real) + abs(final_coord.imag)}")


if __name__ == "__main__":
    main()
