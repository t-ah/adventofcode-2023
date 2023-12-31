from pathlib import Path
from collections import defaultdict, deque


directions = {
    "n": (0, -1),
    "s": (0, 1),
    "e": (1, 0),
    "w": (-1, 0)
}

slash_map = {
    "s": "w",
    "w": "s",
    "n": "e",
    "e": "n"
}

backslash_map = {
    "s": "e",
    "e": "s",
    "n": "w",
    "w": "n"
}


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
            grid[x, y] = c
    energies = [get_e_tiles(start_job, grid) for start_job in get_start_jobs(lines)]
    print(max(energies))


def get_start_jobs(lines: list[str]):
    for x in range(len(lines[0])):
        yield ((x, 0), "s")
        yield ((x, len(lines) - 1), "n")
    for y in range(len(lines)):
        yield ((0, y), "e")
        yield ((len(lines[0]) - 1, y), "w")


def get_e_tiles(start_job, grid) -> int:
    visited = set()
    jobs = deque()
    jobs.append(start_job)
    all_jobs = set()
    all_jobs.add(start_job)
    while jobs:
        for new_job in step(jobs, grid, visited):
            if new_job not in all_jobs:
                jobs.append(new_job)
                all_jobs.add(new_job)
    return len(visited)


def step(jobs: deque, grid: dict, visited: set) -> list[tuple[tuple[int, int], str]]:
    job = jobs.pop()
    pos = job[0]
    direction = job[1]
    field = grid[pos]
    if field == "#":
        return []
    visited.add(pos)
    if field == ".":
        return [(moved(pos, direction), direction)]
    elif field == "-":
        dirs = ["e", "w"]
        if direction in dirs:
            return [(moved(pos, direction), direction)]
        else:
            return [(moved(pos, d), d) for d in dirs]
    elif field == "|":
        dirs = ["n", "s"]
        if direction in dirs:
            return [(moved(pos, direction), direction)]
        else:
            return [(moved(pos, d), d) for d in dirs]
    elif field == "/":
        new_direction = slash_map[direction]
        return [(moved(pos, new_direction), new_direction)]
    elif field == "\\":
        new_direction = backslash_map[direction]
        return [(moved(pos, new_direction), new_direction)]
    return []


def moved(pos: tuple[int, int], direction: str) -> tuple[int, int]:
    offset = directions[direction]
    return (pos[0] + offset[0], pos[1] + offset[1])


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
