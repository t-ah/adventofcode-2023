from os import path
import bisect
import sys


class Conversion:
    def __init__(self, destination_start, source_start, ranges) -> None:
        self.source_start = source_start
        self.destination_start = destination_start
        self.ranges = ranges


def main():
    for file_name in ["test/day5_1.txt", "input/day5_1.txt"]:
        if path.exists(file_name):
            solve(file_name)


def solve(file_name: str):
    blocks = read_input(file_name)
    seed_ranges = [int(s) for s in blocks[0][0].split()[1:]]
    conv_maps = []
    for block in blocks[1:]:
        conv_map = []
        conv_maps.append(conv_map)
        for line in block[1:]:
            numbers = line.split()
            conv_map.append(Conversion(int(numbers[0]), int(numbers[1]), int(numbers[2])))
        conv_map.sort(key=lambda conv: conv.destination_start)
    location = 0
    while True:
        if location % 100000 == 0:
            print(location)
        if test_location(location, conv_maps, seed_ranges):
            print(location)
            break
        else:
            location += 1


def test_location(location: int, conv_maps: list, seed_ranges: list):
    seed = find_seed(location, conv_maps)
    for i in range(0, len(seed_ranges), 2):
        if seed >= seed_ranges[i] and seed < seed_ranges[i] + seed_ranges[i + 1]:
            return True
    return False


def find_seed(location: int, conv_maps: list):
    current = location
    for conv_map in reversed(conv_maps):
        index = bisect.bisect_left(conv_map, current, key=lambda conv: conv.destination_start)
        conv_index = index if index < len(conv_map) and conv_map[index].destination_start == current else index - 1
        if conv_index < 0:
            continue  # smaller than smallest destination range start
        conversion = conv_map[conv_index]
        if current >= conversion.destination_start + conversion.ranges:
            continue  # also unmapped
        current += conversion.source_start - conversion.destination_start
    return current


def read_input(file_name):
    with open(file_name, "r") as f:
        return [b.split("\n") for b in f.read().split("\n\n")]


if __name__ == "__main__":
    main()
