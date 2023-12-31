from os import path


def main():
    for file_name in ["test/day1_1.txt", "input/day1.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    lines = read_input(file_name)
    c_values = [int(digit(line, True) + digit(line, False)) for line in lines]
    print(sum(c_values))


def digit(s_in: str, first: bool) -> str:
    s = s_in if first else reversed(s_in)
    for c in s:
        if c.isdigit():
            return c
    raise ValueError(f"No digit in string {s_in}.")


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
