#!/usr/bin/env python3


def contains_required_fields(passport):
    required = ("byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:")
    return all(f in passport for f in required)


with open("input.txt", "r") as batch_file:
    passports = batch_file.read().strip().split("\n\n")

print("Part 1 solution:")
print(sum(contains_required_fields(p) for p in passports))
