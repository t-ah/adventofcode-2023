from pathlib import Path
from collections import defaultdict


moves = {
    "|": ((0, -1), (0, 1)),
    "-": ((1, 0), (-1, 0)),
    "F": ((1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((-1, 0), (0, 1)),
    "L": ((0, -1), (1, 0)),
    ".": (),
    "S": ((1, 0), (0, 1), (-1, 0), (0, -1)),
}


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    grid = defaultdict(lambda: ".")
    start = (0, 0)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                start = (x, y)
    loop = build_loop(grid, start)
    print(len(loop) // 2)


def build_loop(grid: defaultdict[tuple[int, int], str], start: tuple[int, int]):
    position = start
    loop = [position]
    while True:
        neighbours = [neighbour for neighbour in next_positions(grid, position) if position in next_positions(grid, neighbour)]
        neighbour = neighbours[0] if len(loop) == 1 or loop[-2] != neighbours[0] else neighbours[1]
        loop.append(neighbour)
        position = neighbour
        if position == start:
            break
    return loop

def next_positions(grid: defaultdict[tuple[int, int], str], position: tuple[int, int]) -> list[tuple[int, int]]:
    move = grid[position]
    return [(position[0] + offset[0], position[1] + offset[1]) for offset in moves[move]]


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
