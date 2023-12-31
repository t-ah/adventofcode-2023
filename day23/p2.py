"""
Step 1: compress graph
Step 2: get some cookies
Step 3:
"""
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
    for file_name in ["p2-test.txt", "p2-input.txt"]:
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
        if c != "#":
            for n_pos in get_neighbours(x, y):
                if grid[n_pos] != "#":
                    graph[x, y][n_pos] = 1
    compress(graph)
    queue = deque([State(0, start, {start})])
    max_path = 0
    while queue:
        state = queue.popleft()
        possible_next = graph[state.pos].keys() - state.visited
        for n in possible_next:
            length = state.length + graph[state.pos][n]
            if n == goal:
                max_path = max(max_path, length)
            else:
                queue.append(State(length, n, state.visited.union([n])))
    print(max_path)


def compress(graph):
    print("Uncompressed:", len(graph))
    while True:
        prev_length = len(graph)
        for node in list(graph.keys()):
            neighbours = list(graph[node])
            if len(neighbours) != 2:
                continue
            # connect neighbours directly
            n1, n2 = neighbours
            length = graph[node][n1] + graph[node][n2]
            graph[n1][n2] = length
            graph[n2][n1] = length
            del graph[n1][node]
            del graph[n2][node]
            del graph[node]
        if len(graph) == prev_length:
            print("Compressed:", len(graph))
            break


def get_neighbours(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
