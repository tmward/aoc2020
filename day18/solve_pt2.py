#!/usr/bin/env python3
import re
import sys

def get_input(filename):
    with open(filename, 'r') as f:
        return [l.strip().replace(" ", "") for l in f]


def calculate(problem):
    # Greedy matching makes this regex more complicated. Need to first
    # match either the beginning then immediately the the n1 + n2 or a
    # bunch of expressions before then n1 + n2. You can't just do greedy
    # to start because it'll snatch beginning digits from n1 (e.g. if
    # it's 210 it'll snatch 21 so n1 is falsely set to 0
    if (m := re.match(r"(^|^(.+[\+\*]))*(\d+\+\d+)(.*)$", problem)):
        return calculate(m.group(1) + str(eval(m.group(3))) + m.group(4))
    return eval(problem)


def solution(problem):
    if (m := re.match(r"^(.*)\(([^\(\)]+)\)(.*)$", problem)):
        return solution(m.group(1) + str(calculate(m.group(2))) + m.group(3))
    return calculate(problem)


def solve(problems):
    return sum(solution(p) for p in problems)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: sys.argv[0] inputfile")
        sys.exit(2)
    print(f"Pt 2 answer: {solve(get_input(sys.argv[1]))}")


if __name__ == "__main__":
    main()
