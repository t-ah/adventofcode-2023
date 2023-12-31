from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    sum = 0
    for line in lines:
        pattern, counts = line.split(" ", 1)
        pattern += "."
        counts = [int(count) for count in counts.split(",")]
        sum += count_arrangements(pattern, counts, 0)
    print(sum)


def count_arrangements(pattern: str, counts: list[int], start_index) -> int:
    index = pattern.find('?', start_index)
    if index == -1:
        return 1 if is_valid(pattern, counts) else 0
    pre = pattern[:index]
    post = pattern[index + 1:]
    return count_arrangements(f"{pre}#{post}", counts, index + 1) + count_arrangements(f"{pre}.{post}", counts, index + 1)


def is_valid(pattern: str, counts: list[int]) -> bool:
    count_index = 0
    current_count = 0
    for c in pattern:
        if c == "#":
            current_count += 1
        elif current_count > 0:
            if count_index >= len(counts) or current_count != counts[count_index]:
                return False
            current_count = 0
            count_index += 1
    return count_index == len(counts)


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
