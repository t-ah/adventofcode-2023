from pathlib import Path


directions = {
    "0": (0, 1),
    "2": (0, -1),
    "3": (-1, 0),
    "1": (1, 0),
}


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    position = (0, 0)
    vertices = []

    length_sum = 0
    for line in lines:
        code = line.split(" ")[2]
        direction = code[-2]
        length = int(code[2 : -2], 16)
        length_sum += length
        position = moved(position, direction, length)
        vertices.append(position)
    result = 0
    for i in range(len(vertices) - 1):
        a = vertices[i]
        b = vertices[i + 1]
        result += (a[1] + b[1]) * (a[0] - b[0])
    print(vertices[0])
    a = vertices[-1]
    b = vertices[0]
    result += (a[1] + b[1]) * (a[0] - b[0])
    print(abs(result // 2) + length_sum // 2 + 1)


def moved(position, direction, length):
    offset = directions[direction]
    return (position[0] + length * offset[0], position[1] + length * offset[1])


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
