#!/usr/bin/env python3
import re
import sys


def fix_type(d, a):
    return (d, int(a))


def get_input(filename):
    rgx = re.compile(r"([A-Z]+)(\d+)")
    with open(filename, "r") as ifile:
        return [fix_type(*m.groups()) for l in ifile if (m := rgx.match(l))]


def rotate(d_faced, direction, degree):
    d_to_angle = {"E": 0, "N": 90, "W": 180, "S": 270}
    angle_to_d = {0: "E", 90: "N", 180: "W", 270: "S"}
    start = d_to_angle.get(d_faced)
    if direction == "R":
        degree *= -1
    return angle_to_d.get((360 + start + degree) % 360)


def advance(coord, direction, amount):
    d_to_i = {
        "E": complex(1),
        "N": complex(0, 1),
        "W": complex(-1),
        "S": complex(0, -1),
    }
    return coord + d_to_i.get(direction) * amount


def follow(d_and_as):
    d_faced = "E"
    coord = complex(0, 0)
    for new_d, a in d_and_as:
        if new_d in ("R", "L"):
            d_faced = rotate(d_faced, new_d, a)
        elif new_d == "F":
            coord = advance(coord, d_faced, a)
        else:
            coord = advance(coord, new_d, a)
    return coord


def main():
    if len(sys.argv) != 2:
        print("usage: ./solve.py inputfile")
        sys.exit(2)
    d_and_as = get_input(sys.argv[1])
    final_coord = follow(d_and_as)
    print(f"Part 1 answer: {abs(final_coord.real) + abs(final_coord.imag)}")


if __name__ == "__main__":
    main()
