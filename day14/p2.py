from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    grid = defaultdict(lambda: "#")
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x,y] = c
    cache = {}
    i = 0
    iterations = 1000000000
    while i < iterations:
        cycle(grid, lines)
        config = get_config(grid)
        if config in cache:
            loop = i - cache[config]
            remaining_cycles = iterations - i
            remaining_after_skip = remaining_cycles % loop
            i = iterations - remaining_after_skip
        else:
            cache[config] = i
        i += 1
    print(get_load(grid, len(lines)))


def get_config(grid):
    return tuple(sorted([k for k in grid if grid[k] == "O"]))


def cycle(grid, lines):
    y_start, x_start = 0, 0
    x_end = len(lines[0]) - 1
    y_end = len(lines) -1
    roll(grid, 0, -1, range(y_start, y_end + 1), range(x_start, x_end + 1))
    roll(grid, -1, 0, range(y_start, y_end + 1), range(x_start, x_end + 1))
    roll(grid, 0, 1, range(y_end, y_start -1, -1), range(x_start, x_end + 1))
    roll(grid, 1, 0, range(y_start, y_end + 1), range(x_end, x_start - 1, - 1))
    

def roll(grid, ox, oy, range_y, range_x):
    for y in range_y:
        for x in range_x:
            if grid[x, y] == "O":
                push(x, y, grid, ox, oy)


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
