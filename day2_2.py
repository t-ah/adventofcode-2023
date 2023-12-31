from os import path


colours = ["red", "green", "blue"]


class Draw:
    def __init__(self) -> None:
        self.cubes = dict()
        for colour in colours:
            self.cubes[colour] = 0


class Game:
    def __init__(self) -> None:
        self.draws: list[Draw] = []

    def is_feasible(self) -> bool:
        for draw in self.draws:
            if draw.cubes["red"] > 12 or draw.cubes["green"] > 13 or draw.cubes["blue"] > 14:
                return False
        return True
    
    def power(self) -> int:
        max_cubes = {colour: 0 for colour in colours}
        for draw in self.draws:
            for colour in colours:
                max_cubes[colour] = max(max_cubes[colour], draw.cubes[colour])
        return max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]


def main():
    for file_name in ["test/day2_2.txt", "input/day2_2.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    game_list: list[Game] = []
    lines = read_input(file_name)
    games = [line.split(": ", 1)[1] for line in lines]
    for game in games:
        new_game = Game()
        game_list.append(new_game)
        draws = game.split("; ")
        for draw in draws:
            new_draw = Draw()
            new_game.draws.append(new_draw)
            items = draw.split(", ")
            for item in items:
                parts = item.split(" ", 1)
                amount, colour = int(parts[0]), parts[1]
                new_draw.cubes[colour] = amount
    print(sum([game.power() for game in game_list]))


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
