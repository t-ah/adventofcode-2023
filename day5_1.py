from os import path
import bisect


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
    seeds = [int(s) for s in blocks[0][0].split()[1:]]
    conv_maps = []
    for block in blocks[1:]:
        conv_map = []
        conv_maps.append(conv_map)
        for line in block[1:]:
            numbers = line.split()
            conv_map.append(Conversion(int(numbers[0]), int(numbers[1]), int(numbers[2])))
        conv_map.sort(key=lambda conv: conv.source_start)
    locations = [find_location(seed, conv_maps) for seed in seeds]
    print(min(locations))

def find_location(seed: int, conv_maps: list):
    current = seed
    for conv_map in conv_maps:
        index = bisect.bisect_left(conv_map, current, key=lambda conv: conv.source_start)
        if index == 0:
            continue  # smaller than smallest source range start
        conversion = conv_map[index - 1]
        if current >= conversion.source_start + conversion.ranges:
            continue  # also unmapped
        current += conversion.destination_start - conversion.source_start
    return current


def read_input(file_name):
    with open(file_name, "r") as f:
        return [b.split("\n") for b in f.read().split("\n\n")]


if __name__ == "__main__":
    main()
