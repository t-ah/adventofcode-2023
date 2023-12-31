from pathlib import Path
import numpy as np


# Hello. This was not my day, so to say.

class Infinigrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._grid = {}

    def set(self, x, y, content):
        self._grid[x, y] = content

    def get(self, x, y):
        return self._grid[x % self.width, y % self.height]

    def find_start(self):
        for pos, entry in self._grid.items():
            if entry == "S":
                return pos
        raise ValueError("No start in grid.")


def main():
    for file_name in ["p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    grid = build_grid(lines)
    start = grid.find_start()
    new_positions = set()
    new_positions.add(start)
    even = set()
    odd = set()
    even.add(start)
    steps = 26501365
    rem = steps % len(lines)
    relevant_indices = [i * len(lines) + rem for i in range(3)]
    results = []
    for i in range(1, steps):
        adjacent_nodes = adjacent(new_positions, grid)
        new_positions = set()
        for n in adjacent_nodes:
            if n in even or n in odd:
                continue
            new_positions.add(n)
            if i % 2 == 0:
                even.add(n)
            else:
                odd.add(n)
        if i in relevant_indices:
            results.append(len(even) if i % 2 == 0 else len(odd))
        if i == relevant_indices[-1]:
            break
    n = (steps - rem) // len(lines)
    p = np.polyfit(list(range(len(results))), results, 2)
    result = np.polyval(p, n)
    print(result)


def adjacent(positions: set[tuple[int, int]], grid) -> set[tuple[int, int]]:
    new_positions = set()
    for position in positions:
        new_positions.update([n for n in neighbours(position) if grid.get(*n) != "#"])
    return new_positions


def build_grid(lines):
    grid = Infinigrid(len(lines[0]), len(lines))
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid.set(x, y, c)
    return grid


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
