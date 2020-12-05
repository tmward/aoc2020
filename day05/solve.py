#!/usr/bin/env python3

# 128 rows in the plane
def row(spec, rows=range(128)):
    return {
        "F": row(spec[1:], rows[:len(rows) // 2]),
        "B": row(spec[1:], rows[len(rows) // 2 :]),
    }[spec[0]] if spec else rows[0]


# 8 columns (seats per row) in the plane
def column(spec, cols=range(8)):
    return {
        "L": column(spec[1:], cols[:len(cols) // 2]),
        "R": column(spec[1:], cols[len(cols) // 2 :]),
    }[spec[0]] if spec else cols[0]


def seat_id(row, column):
    return row * 8 + column


with open("input.txt", "r") as input_file:
    # seats tuple of (Row specification, Column spec)
    seats = [(l[:7], l[7:]) for l in input_file.read().splitlines()]

seat_ids = {seat_id(row(r), column(c)) for r, c in seats}
print("Part 1 solution")
print(max(seat_ids))

print("Part 2 solution")
print(seat_ids ^ {*range(min(seat_ids), max(seat_ids) + 1)})
