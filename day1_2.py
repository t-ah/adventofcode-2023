from os import path

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def main():
    for file_name in ["test/day1_2.txt", "input/day1.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    lines = read_input(file_name)
    c_values = [int(digit(line, True) + digit(line, False)) for line in lines]
    print(sum(c_values))


def digit(s_in: str, first: bool) -> str:
    word_order = enumerate(s_in) if first else reversed(list(enumerate(s_in)))
    for i, c in word_order:
        if c.isdigit():
            return c
        sub = s_in[i:]
        for number_word, number in numbers.items():
            if sub.startswith(number_word):
                return number
    raise ValueError(f"No digit in string {s_in}.")


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
