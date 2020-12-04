#!/usr/bin/env python3
from functools import partial
import re


def contains_required_fields(passport):
    required = ("byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:")
    return all(f in passport for f in required)


def parse(passport):
    # returns (k, v) for each passport field
    return [f.split(":") for f in passport.replace(" ", "\n").splitlines()]


def valid_number(low, high, num):
    try:
        return low <= int(num) <= high
    except ValueError:
        return False


def valid_height(value):
    if len(value) >= 4:
        unit = value.strip()[-2:]
        val = value.strip()[:-2]
        return (unit == "cm" and valid_number(150, 193, val)) or (
            unit == "in" and valid_number(59, 76, val)
        )

    return False


def valid_hair_color(value):
    return bool(re.fullmatch(r"#[0-9a-f]{6}", value))


def valid_eye_color(value):
    eye_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    return any(value == eye_color for eye_color in eye_colors)


def valid_passport_number(value):
    return bool(re.fullmatch(r"[0-9]{9}", value))


def always_true(*args, **kwargs):
    return True


def is_valid_field(k, v):
    return {
        "byr": partial(valid_number, 1920, 2002),
        "iyr": partial(valid_number, 2010, 2020),
        "eyr": partial(valid_number, 2020, 2030),
        "hgt": valid_height,
        "hcl": valid_hair_color,
        "ecl": valid_eye_color,
        "pid": valid_passport_number,
    }.get(k, always_true)(v)


def is_valid_passport(passport):
    return all(is_valid_field(k, v) for k, v in passport)


def main():
    with open("input.txt", "r") as batch_file:
        passports = batch_file.read().strip().split("\n\n")

    print("Part 1 solution:")
    print(sum(contains_required_fields(p) for p in passports))

    print("Part 2 solution:")
    print(
        sum(
            map(
                is_valid_passport,
                map(parse, filter(contains_required_fields, passports)),
            )
        )
    )


if __name__ == "__main__":
    main()
