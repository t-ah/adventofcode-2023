from os import path


def main():
    for file_name in ["test/day6_1.txt", "input/day6_1.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    lines = read_input(file_name)
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    start = search(time, distance, 0, time, True)
    end = search(time, distance, start, time, False)
    print(end - start)


def search(time: int, distance: int, left: int, right: int, find_feasible: bool):
    bound_left = left
    bound_right = right
    while bound_left + 1 < bound_right:
        current = bound_left + ((bound_right - bound_left) // 2)
        if is_feasible(time, distance, current) == find_feasible:
            bound_right = current
        else:
            bound_left = current
    return bound_right


def is_feasible(time: int, distance: int, charge: int) -> bool:
    return (time - charge) * charge > distance


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
