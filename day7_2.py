from os import path
from functools import cmp_to_key
from collections import Counter


values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}


class Hand():
    def __init__(self, line: str) -> None:
        self.cards = line[:5]
        self.bid = int(line[6:])

    def get_type(self) -> int:
        counter = Counter(self.cards)
        jokers = counter["J"]
        counter.subtract("JJJJJ")
        counts = counter.most_common()
        if counts[0][1] + jokers == 5:
            return 7
        if counts[0][1] + jokers == 4:
            return 6
        if counts[0][1] + jokers == 3:
            if counts[1][1] == 2:
                return 5
            else:
                return 4
        if counts[0][1] + jokers == 2:
            if counts[1][1] == 2:
                return 3
            else:
                return 2
        return 1


def main():
    for file_name in ["test/day7_1.txt", "input/day7_1.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    hands = [Hand(line) for line in read_input(file_name)]
    sum = 0
    for i, hand in enumerate(sorted(hands, key=cmp_to_key(compare_by_type))):
        sum += (i + 1) * hand.bid
    print(sum)


def compare_by_type(h1: Hand, h2: Hand) -> int:
    t1, t2 = h1.get_type(), h2.get_type()
    if t1 < t2:
        return -1
    if t1 > t2:
        return 1
    return compare_by_value(h1.cards, h2.cards)


def compare_by_value(c1: str, c2: str) -> int:
    for i in range(len(c1)):
        v1, v2 = values[c1[i]], values[c2[i]]
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
    return 0


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
