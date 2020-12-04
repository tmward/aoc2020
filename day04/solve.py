#!/usr/bin/env python3
from pprint import pprint


def is_valid(passport):
    required = ("byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:")
    return all(x in passport for x in required)


with open("input.txt", "r") as batch_file:
    passports = batch_file.read().strip().split("\n\n")

print("Part 1 solution:")
print(sum(is_valid(p) for p in passports))
