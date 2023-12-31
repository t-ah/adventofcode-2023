from pathlib import Path
from collections import defaultdict


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    grid = build_grid(lines)
    start = find_start(grid)
    positions = set()
    positions.add(start)
    for _ in range(64):
        positions = adjacent(positions, grid)
    print(len(positions))


def adjacent(positions: set[tuple[int,int]], grid) -> set[tuple[int, int]]:
    new_positions = set()
    for position in positions:
        new_positions.update([n for n in neighbours(position) if grid[n] != "#"])
    return new_positions


def build_grid(lines):
    grid = defaultdict(lambda: "#")
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = c
    return grid


def find_start(grid):
    for pos, entry in grid.items():
        if entry == "S":
            return pos
    raise ValueError("No start in grid.")


def neighbours(p):
    yield p[0] + 1, p[1]
    yield p[0] - 1, p[1]
    yield p[0], p[1] + 1
    yield p[0], p[1] - 1


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
