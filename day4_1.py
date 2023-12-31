from os import path


class Card():
    def __init__(self, numbers: str) -> None:
        winning, actual = numbers.split(" | ")
        self.winning = set(winning.split())
        self.numbers = actual.split()
    
    def get_points(self):
        matches = [n for n in self.numbers if n in self.winning]
        if len(matches) > 0:
            return pow(2, len(matches) - 1)
        return 0


def main():
    for file_name in ["test/day4_1.txt", "input/day4_1.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    cards = [Card(line.split(": ")[1]) for line in read_input(file_name)]
    points = [card.get_points() for card in cards]
    print(sum(points))


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
