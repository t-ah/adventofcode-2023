from os import path
from collections import defaultdict
import re


def main():
    for file_name in ["test/day3_1.txt", "input/day3_1.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    lines = read_input(file_name)
    grid = defaultdict(lambda: ".")
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            grid[(x, y)] = lines[y][x]
    gears = defaultdict(lambda: list())
    for y in range(len(lines)):
        for match in re.finditer(r'\d+', lines[y]):
            start, end = match.span()
            assign(start, end, y, grid, gears, int(match.group()))
    result = 0
    for pos in gears:
        gear = gears[pos]
        if len(gear) == 2:
            result += gear[0] * gear[1]
    print(result)


def assign(start, end, y, grid, gears, n):
    for offset in [-1, 0, 1]:
        check(start - 1, y + offset, grid, gears, n)
        check(end, y + offset, grid, gears, n)
    for offset in [-1, 1]:
        for x in range(start, end):
            check(x, y + offset, grid, gears, n)


def check(x, y, grid, gears, n):
    if grid[(x, y)] == "*":
        gears[(x, y)].append(n)


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
