from pathlib import Path


class Lens():
    def __init__(self, label: str, strength: int) -> None:
        self.label = label
        self.strength = strength


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    steps = lines[0].split(",")
    boxes = [[] for _ in range(256)]
    for step in steps:
        if step[-1] == "-":
            label = step[:-1]
            remove(boxes, label)
        else:
            label, nr = step.split("=", 1)
            add(boxes, label, int(nr))
    result = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            result += (i + 1) * (j + 1) * lens.strength
    print(result)


def remove(boxes, label):
    box_id = get_hash(label)
    boxes[box_id] = [lens for lens in boxes[box_id] if lens.label != label]


def add(boxes, label, nr):
    box_id = get_hash(label)
    box = boxes[box_id]
    for lens in box:
        if lens.label == label:
            lens.strength = nr
            return
    boxes[box_id].append(Lens(label, nr))


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
