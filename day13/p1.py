from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(patterns: list[str]):
    print(sum([get_value(pattern.split("\n")) for pattern in patterns]))


def get_value(lines: list[str]) -> int:
    v = find_axis(lines)
    if v != -1:
        return 100 * v
    else:
        return find_axis(flipped(lines))


def find_axis(lines: list[str]) -> int:
    for axis in range(1, len(lines)):
        if mirrors(lines, axis):
            return axis
    return -1


# whether lines before axis index are mirror copies of those below
def mirrors(lines: list[str], axis: int) -> bool:
    for i in range(axis):
        upper_line_index = axis - i - 1
        lower_line_index = axis + i
        if upper_line_index < 0 or lower_line_index >= len(lines):
            return True
        if lines[upper_line_index] != lines[lower_line_index]:
            return False
    return True


def flipped(lines: list[str]) -> list[str]:
    new_lines = [""] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            new_lines[i] += c
    return new_lines


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
