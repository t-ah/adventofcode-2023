from os import path
from functools import reduce


def main():
    for file_name in ["test/day6_1.txt", "input/day6_1.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    lines = read_input(file_name)
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]
    ways = [how_many_ways(time, distance) for time, distance in zip(times, distances)]
    print(reduce(lambda x, y: x * y, ways))


def how_many_ways(time: int, distance: int) -> int:
    start = -1
    end = time
    for i in range(1, time):
        if (time - i) * i > distance:
            if start == -1:
                start = i
        elif start != -1:
            end = i
            break
    return end - start


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
