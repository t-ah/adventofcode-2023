from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    steps = lines[0].split(",")
    values = [get_hash(step) for step in steps]
    print(sum(values))


def get_hash(s: str) -> int:
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result %= 256
    return result


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
