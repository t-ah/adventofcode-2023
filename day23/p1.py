from dataclasses import dataclass
from pathlib import Path
from collections import defaultdict, deque


DIRECTIONS = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}


@dataclass
class State:
    length: int
    pos: tuple[int, int]
    visited: set[tuple[int, int]]


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    start = (1, 0)
    goal = len(lines[0]) - 2, len(lines) - 1
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = c
    for pos in [(1, -1), (len(lines[0]) - 2, len(lines))]:
        grid[pos] = "#"
    graph = defaultdict(lambda: defaultdict(lambda: 0))
    for (x, y), c in grid.items():
        if c == ".":
            for n_pos in neighbours(x, y):
                if grid[n_pos] != "#":
                    graph[x, y][n_pos] = 1
        elif c in DIRECTIONS:
            n_pos = x + DIRECTIONS[c][0], y + DIRECTIONS[c][1]
            if grid[n_pos] != "#":
                graph[x, y][n_pos] = 1
    visited_start = set()
    visited_start.add(start)
    queue = deque([State(0, start, visited_start)])
    max_path = 0
    while queue:
        state = queue.popleft()
        possible_next = graph[state.pos].keys() - state.visited
        for n in possible_next:
            if n == goal:
                max_path = max(max_path, state.length + 1)
            else:
                queue.append(State(state.length + 1, n, state.visited.union([n])))
    print(max_path)


def neighbours(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
