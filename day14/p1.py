from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    grid = defaultdict(lambda: "#")
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x,y] = c
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if grid[x, y] == "O":
                push(x, y, grid, 0, -1)
    print(get_load(grid, len(lines)))


def push(x, y, grid, ox, oy):
    new_x, new_y = x, y
    while grid[new_x + ox, new_y + oy] == ".":
        new_x += ox
        new_y += oy
    grid[x, y] = "."
    grid[new_x, new_y] = "O"


def get_load(grid, height):
    result = 0
    for (_, y), c in grid.items():
        if c == "O":
            result += height - y
    return result


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
