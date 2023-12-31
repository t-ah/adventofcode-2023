from pathlib import Path
from functools import cache


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    sum = 0
    for line in lines:
        pattern, counts = line.split(" ", 1)

        pattern = "?".join(5 * [pattern])
        counts = [int(count) for count in counts.split(",")]
        counts = 5 * counts
        sum += count_arrangements(pattern, tuple(counts), 0)
    print(sum)


@cache
def count_arrangements(pattern: str, counts: tuple[int], current_length: int) -> int:
    if not pattern:
        if (current_length == 0 and len(counts) == 0):
            return 1
        if len(counts) == 1 and counts[0] == current_length:
            return 1
        return 0
    if not counts and current_length:
        return 0
    if pattern[0] == ".":
        if current_length and counts and current_length != counts[0]:
            return 0
        return count_arrangements(pattern[1:], counts[1:] if current_length else counts, 0)
    if pattern[0] == "#":
        return count_arrangements(pattern[1:], counts, current_length + 1)
    # case "?":
    if not counts or counts[0] == current_length:
        return count_arrangements(pattern[1:], counts[1:], 0)
    if current_length:
        return count_arrangements(pattern[1:], counts, current_length + 1)
    return count_arrangements(pattern[1:], counts, 0) + count_arrangements(pattern[1:], counts, 1)


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
