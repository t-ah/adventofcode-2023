from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    histories = [map(lambda x: int(x), line.split(" ")) for line in lines]
    next_values = [get_next_value(h) for h in histories]
    print(sum(next_values))


def get_next_value(history) -> int:
    rows = []
    rows.append(list(history))
    while not all(v == 0 for v in rows[-1]):
        differences = [rows[-1][i] - rows[-1][i - 1] for i in range(1, len(rows[-1]))]
        rows.append(differences)
    last_value = 0
    for i in reversed(range(len(rows) - 1)):
        last_value = rows[i][-1] + last_value
    return last_value


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
