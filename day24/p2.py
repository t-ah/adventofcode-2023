from pathlib import Path
from z3 import *


class LineData:
    def __init__(self, line: str):
        left, right = line.split(" @ ")
        self.pos = [int(n) for n in left.split(", ")]
        self.vel = [int(n) for n in right.split(", ")]


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            run(lines)


def run(str_lines: list[str]):
    lines = [LineData(str_line) for str_line in str_lines]
    ps = Ints('px py pz')
    vs = Ints('vx vy vz')
    ts = Ints('t0 t1 t2')
    result = Int('result')

    equations = [ps[i] + ts[j] * vs[i] == lines[j].pos[i] + ts[j] * lines[j].vel[i] for i in range(3) for j in range(3)]

    # equations = [
    #     px + t0 * vx == 260252047346974 + t0 * 66,
    #     py + t0 * vy == 360095837456982 + t0 * -174,
    #     pz + t0 * vz == 9086018216578 + t0 * 512,
    #
    #     px + t1 * vx == 511477129668052 + t1 * -386,
    #     py + t1 * vy == 548070416165820 + t1 * -384,
    #     pz + t1 * vz == 520727565082156 + t1 * -322,
    #
    #     px + t2 * vx == 358771388883194 + t2 * 88,
    #     py + t2 * vy == 290970068566246 + t2 * -82,
    #     pz + t2 * vz == 208977773545854 + t2 * 254,
    # ]

    solve(
        *equations,
        result == ps[0] + ps[1] + ps[2],
    )


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
