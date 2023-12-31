from pathlib import Path


replacements = {".": "#", "#": "."}


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(patterns: list[str]):
    print(sum([get_value_with_change(pattern.split("\n")) for pattern in patterns]))


# the main "problem" is ignoring the original axis if it would still apply
def get_value_with_change(lines: list[str]) -> int:
    original_value = get_value(lines)
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            lines[i] = line[:j] + replacements[line[j]] + line[j + 1:]
            v = get_value(lines, ignore=original_value)
            if v != -1:
                return v
            lines[i] = line
    raise ValueError("Everything is broken, send help")


def get_value(lines: list[str], ignore=-1) -> int:
    v = find_axis(lines, ignore, factor=100)
    if v != -1:
        return 100 * v
    else:
        return find_axis(flipped(lines), ignore)


def find_axis(lines: list[str], ignore=-1, factor=1) -> int:
    for axis in range(1, len(lines)):
        if mirrors(lines, axis) and factor * axis != ignore:
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