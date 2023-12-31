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
    for file_name in ["p2-test.txt", "p2-input.txt"]:
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
    replace_start(grid, loop, start)
    x_min = min(loop, key=lambda p: p[0])[0]
    x_max = max(loop, key=lambda p: p[0])[0]
    y_min = min(loop, key=lambda p: p[1])[1]
    y_max = max(loop, key=lambda p: p[1])[1]
    count = 0
    loop_set = set(loop)
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if is_inside(x, y, grid, loop_set, x_max):
                count += 1
    print(count)


def is_inside(x, y, grid, loop, x_max):
    if (x, y) in loop:
        return False
    walls = []
    for xi in range(x + 1, x_max + 1):
        if (xi, y) in loop and grid[(xi, y)] not in (".", "-"):
            walls.append(grid[xi, y])
    outside = True
    for i, wall_type in enumerate(walls):
        if wall_type == "|" or (wall_type == "7" and walls[i - 1] == "L") or (wall_type == "J" and walls[i - 1] == "F"):
            outside = not outside
    return not outside


def replace_start(grid, loop, start):
    neighbours = [loop[1], loop[-2]]
    offsets = [get_offset(nbr, start) for nbr in neighbours]
    for move in moves:
        target_offsets = moves[move]
        if offsets[0] in target_offsets and offsets[1] in target_offsets:
            grid[start] = move
            return


def get_offset(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])


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
