from pathlib import Path
import numpy as np
from PIL import Image


directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    grid = {}
    grid[0, 0] = "#ffffff"
    position = (0, 0)
    for line in lines:
        parts = line.split(" ")
        direction = parts[0]
        length = int(parts[1])
        color = parts[2][1:-1]
        for _ in range(length):
            position = moved(position, direction)
            grid[position] = color
    infill = fill(grid)
    print(len(infill) + len(grid))
    # show_image(grid)


def show_image(grid):
    x_max = max((p[0] for p in grid))
    y_max = max((p[1] for p in grid))
    x_min = min((p[0] for p in grid))
    y_min = min((p[1] for p in grid))
    img = Image.new( 'RGB', (y_max - y_min + 1, x_max - x_min + 1), "black")
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = hex_to_rgb(grid[j + x_min, i+y_min]) if (j + x_min, i+y_min) in grid else (0, 0, 0)
    img.show()


def hex_to_rgb(hex: str):
    value = hex[1:]
    lv = len(value)
    return tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))


def fill(grid):
    fillings = set()
    new_fillings = set()
    fillings.add((1,1))
    new_fillings.add((1,1))
    while new_fillings:
        to_expand = new_fillings
        new_fillings = set()
        for p in to_expand:
            for n in neighbours(p):
                if n not in grid and n not in fillings:
                    fillings.add(n)
                    new_fillings.add(n)
    return fillings


def neighbours(p):
    yield p[0] + 1, p[1]
    yield p[0] - 1, p[1]
    yield p[0], p[1] + 1
    yield p[0], p[1] - 1


def moved(position, direction):
    offset = directions[direction]
    return (position[0] + offset[0], position[1] + offset[1])


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
