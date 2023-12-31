from os import path


class Card():
    def __init__(self, numbers: str) -> None:
        self.copies = 1
        winning, actual = numbers.split(" | ")
        self.winning = set(winning.split())
        self.numbers = actual.split()


def main():
    for file_name in ["test/day4_2.txt", "input/day4_2.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    cards = [Card(line.split(": ")[1]) for line in read_input(file_name)]
    for i, card in enumerate(cards):
        matches = [n for n in card.numbers if n in card.winning]
        for j in range(i + 1, min(i + 1 + len(matches), len(cards))):
            cards[j].copies += card.copies
    print(sum([card.copies for card in cards]))


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
