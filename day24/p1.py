from pathlib import Path
import sympy


class LineData:
    def __init__(self, line: str):
        left, right = line.split(" @ ")
        self.pos = [int(n) for n in left.split(", ")]
        self.vel = [int(n) for n in right.split(", ")]


def main():
    for file_name, bounds in [("p1-test.txt", (7, 27)), ("p1-input.txt", (200000000000000.0, 400000000000000.0))]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines, bounds)


def solve(str_lines: list[str], bounds: tuple[int, int]):
    lines = [LineData(str_line) for str_line in str_lines]
    count = 0
    for i, line1 in enumerate(lines):
        for line2 in lines[i + 1:]:
            solutions = get_intersection(line1, line2)
            if len(solutions) != 1:
                continue
            for solution in solutions:
                r, s = solution
                ix, iy = [line1.pos[i] + r * line1.vel[i] for i in range(2)]
                if bounds[0] <= ix <= bounds[1] and bounds[0] <= iy <= bounds[1]:
                    if is_future_point(line1, (ix, iy)) and is_future_point(line2, (ix, iy)):
                        count += 1
    print(count)


def get_intersection(line1, line2, dim=2):
    a = sympy.Matrix([[line1.vel[i], -line2.vel[i]] for i in range(dim)])
    b = sympy.Matrix([[line2.pos[i] - line1.pos[i]] for i in range(dim)])
    return sympy.solvers.linsolve((a, b))


def is_future_point(line, point) -> bool:
    for d in [0, 1]:
        if line.vel[d] > 0:
            if point[d] <= line.pos[d]:
                return False
        elif line.vel[d] < 0:
            if point[d] >= line.pos[d]:
                return False
    return True


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
