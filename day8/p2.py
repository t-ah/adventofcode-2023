from pathlib import Path
from itertools import chain


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    instructions = lines[0]
    left, right = dict(), dict()
    positions = []
    for line in lines[2:]:
        start = line[:3]
        left[start] = line[7:10]
        right[start] = line[12:15]
        if start[2] == "A":
            positions.append(start)
    step = 0
    offsets = [0 for _ in positions]
    loops = [0 for _ in positions]
    while not finished(loops):
        instruction = instructions[step % len(instructions)]
        step += 1
        relevant_dict = left
        if instruction == "R":
            relevant_dict = right
        positions = [relevant_dict[p] for p in positions]
        for i, p in enumerate(positions):
            if p[2] == "Z":
                if offsets[i] == 0:
                    offsets[i] = step
                else:
                    if loops[i] == 0:
                        loops[i] = step - offsets[i]
    steps = offsets
    # we could solve some nice equations probably, but we can also get a coffee and heat our home/office:
    max_loop = max(loops)
    max_loop_index = loops.index(max_loop)
    while not all_equal(steps):
        steps[max_loop_index] += max_loop
        for i in chain(range(max_loop_index), range(max_loop_index + 1, len(positions))):
            while steps[i] < steps[max_loop_index]:
                steps[i] += loops[i]
    print(steps[0])


def all_equal(steps: list[int]) -> bool:
    v = steps[0]
    for s in steps:
        if s != v:
            return False
    return True


def finished(loops: list[int]) -> bool:
    for l in loops:
        if l == 0:
            return False
    return True


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
