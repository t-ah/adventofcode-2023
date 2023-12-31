from pathlib import Path


class Cube:
    def __init__(self, line: str):
        e1, e2 = line.split("~")
        self.x1, self.y1, self.z1 = [int(x) for x in e1.split(",")]
        self.x2, self.y2, self.z2 = [int(x) for x in e2.split(",")]
        self.on_top: set[Cube] = set()
        self.below: set[Cube] = set()

    def lower(self, base_z):
        distance = self.z1 - base_z - 1
        self.z1 -= distance
        self.z2 -= distance

    def overlaps(self, other: "Cube"):
        return self._overlaps_x(other) and self._overlaps_y(other)

    def _overlaps_x(self, other):
        return not other.x2 < self.x1 and not other.x1 > self.x2

    def _overlaps_y(self, other):
        return not other.y2 < self.y1 and not other.y1 > self.y2

    def add_on_top(self, other: "Cube"):
        self.on_top.add(other)

    def add_below(self, other: "Cube"):
        self.below.add(other)


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def settle(cubes, cube, i):
    overlap_cubes = [c for c in cubes[:i] if c.overlaps(cube)]
    if not overlap_cubes:
        cube.lower(0)
        return
    max_z = max(overlap_cubes, key=lambda c: c.z2).z2
    base_cubes = [c for c in overlap_cubes if c.z2 == max_z]
    for other_cube in base_cubes:
        other_cube.add_on_top(cube)
        cube.add_below(other_cube)
        cube.lower(other_cube.z2)


def is_disintegratable(cube: Cube):
    for other in cube.on_top:
        if len(other.below) == 1:
            return False
    return True


def solve(lines: list[str]):
    cubes = sorted([Cube(line) for line in lines], key=lambda c: c.z1)
    for i, cube in enumerate(cubes):
        settle(cubes, cube, i)
    disintegratable = [c for c in cubes if is_disintegratable(c)]
    print(len(disintegratable))


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
