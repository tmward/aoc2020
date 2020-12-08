#!/usr/bin/env python3
from pprint import pprint

with open("input.txt", "r") as ifile:
    orig_instructions = []
    for l in ifile:
        op, arg = l.strip().split()
        orig_instructions.append({'op': op, 'arg': int(arg)})

def run(instructions):
    accumulator = 0
    seen = [False] * len(instructions)
    i = 0
    while True:
        if seen[i]:
            print("Instruction already seen")
            return accumulator
        seen[i] = True
        op = instructions[i]['op']
        arg = instructions[i]['arg']
        if op == 'nop':
            i += 1
        elif op == 'acc':
            accumulator += arg
            i += 1
        elif op == 'jmp':
            i += arg


print(f"Part 1 solution: {run(orig_instructions)}")
