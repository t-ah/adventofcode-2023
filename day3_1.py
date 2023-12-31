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
    part_numbers = []
    for y in range(len(lines)):
        for match in re.finditer(r'\d+', lines[y]):
            start, end = match.span()
            if is_part_number(start, end, y, grid):
                part_numbers.append(int(match.group()))
    print(sum(part_numbers))


def is_part_number(start, end, y, grid):
    for offset in [-1, 0, 1]:
        if grid[(start - 1, y + offset)] != ".":
            return True
        if grid[(end, y + offset)] != ".":
            return True
    for offset in [-1, 1]:
        for x in range(start, end):
            if grid[(x, y + offset)] != ".":
                return True
    return False


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
