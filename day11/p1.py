from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    max_x, max_y = len(lines[0]) - 1, len(lines) - 1
    galaxies = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append((x, y))
    free_x = set(range(max_x))
    free_y = set(range(max_y))
    for galaxy in galaxies:
        free_x.discard(galaxy[0])
        free_y.discard(galaxy[1])
    distances = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distances.append(get_distance(galaxies[i], galaxies[j], free_x, free_y))
    print(sum(distances))


def get_distance(pos1, pos2, free_x, free_y) -> int:
    distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    start_x, end_x = min(pos1[0], pos2[0]), max(pos1[0], pos2[0])
    start_y, end_y = min(pos1[1], pos2[1]), max(pos1[1], pos2[1])
    for x in free_x:
        if x > start_x:
            if x < end_x:
                distance += 1
            else:
                break
    for y in free_y:
        if y > start_y:
            if y < end_y:
                distance += 1
            else:
                break
    return distance


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
