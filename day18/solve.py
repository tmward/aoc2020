#!/usr/bin/env python3
import re
import sys

def get_input(filename):
    with open(filename, 'r') as f:
        return [l.strip().replace(" ", "") for l in f]


def calculate(problem):
    exp, rest = re.match(r"^(\d+[\+\-\*\\]\d+)(.*)$", problem).groups()
    ans = eval(exp)
    if rest:
        return calculate(str(ans) + rest)
    else:
        return ans


def solution(problem):
    if (m := re.match(r"^(.*)\(([^\(\)]+)\)(.*)$", problem)):
        return solution(m.group(1) + str(calculate(m.group(2))) + m.group(3))
    else:
        return calculate(problem)
    

def solve(problems):
    return sum(solution(p) for p in problems)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: sys.argv[0] inputfile")
        sys.exit(2)
    print(f"Pt 1 answer: {solve(get_input(sys.argv[1]))}")


if __name__ == "__main__":
    main()
