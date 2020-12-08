#!/usr/bin/env python3
from copy import deepcopy

with open("input.txt", "r") as ifile:
    orig_instructions = []
    for l in ifile:
        op, arg = l.strip().split()
        orig_instructions.append({"op": op, "arg": int(arg)})

# returns (accumulator, index stopped)
def run(instructions):
    accumulator = 0
    not_seen = [True] * len(instructions)
    i = 0
    while i < len(instructions) and not_seen[i]:
        not_seen[i] = False
        op = instructions[i]["op"]
        arg = instructions[i]["arg"]
        if op == "nop":
            i += 1
        elif op == "acc":
            accumulator += arg
            i += 1
        elif op == "jmp":
            i += arg

    return (accumulator, i)


print(f"Part 1 solution: {run(orig_instructions)[0]}")

# Brute force

for i, instruction in enumerate(orig_instructions):
    new_instructions = deepcopy(orig_instructions)
    if instruction["op"] == "nop":
        new_instructions[i]["op"] = "jmp"
    elif instruction["op"] == "jmp":
        new_instructions[i]["op"] = "nop"
    else:
        continue
    acc, idx = run(new_instructions)
    if idx == len(orig_instructions):
        print(f"Part 2 solution: {acc}")
        break
