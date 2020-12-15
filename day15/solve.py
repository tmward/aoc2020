#!/usr/bin/env python3
from collections import defaultdict


def get_input():
    puzzle_input = "5,2,8,16,18,0,1"
    return [int(n) for n in puzzle_input.split(",")]


def solve_pt_1(starting_ns, end):
    counts = {n: turn for turn, n in enumerate(starting_ns[:-1], 1)}
    last_spoken_n = starting_ns[-1]
    for turn in range(len(starting_ns) + 1, end + 1):
        if last_spoken_n not in counts:
            counts[last_spoken_n] = turn - 1
            last_spoken_n = 0
        else:
            to_speak = turn - 1 - counts[last_spoken_n]
            counts[last_spoken_n] = turn - 1
            last_spoken_n = to_speak
    return last_spoken_n



def main():
    starting_ns = get_input()
    print(f"Pt 1 solution: {solve_pt_1(starting_ns, 2020)}")


if __name__ == "__main__":
    main()
