from pathlib import Path


def main():
    for file_name in ["p1-test.txt", "p1-test2.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    instructions = lines[0]
    left, right = dict(), dict()
    for line in lines[2:]:
        start = line[:3]
        left[start] = line[7:10]
        right[start] = line[12:15]
    position = "AAA"
    step = 0
    while position != "ZZZ":
        instruction = instructions[step % len(instructions)]
        step += 1
        if instruction == "L":
            position = left[position]
        else:
            position = right[position]
    print(step)


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
