from pathlib import Path
from collections import defaultdict
import heapq


directions = {
    "E": (1, 0),
    "W": (-1, 0),
    "N": (0, -1),
    "S": (0, 1)
}


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def solve(lines: list[str]):
    graph = defaultdict(lambda: defaultdict(lambda: 0))
    grid = {}
    for y, line in enumerate(lines):
        for x, n in enumerate(line):
            grid[x, y] = int(n)
    width, height = len(lines[0]), len(lines)
    graph[0,0,"-",0][0,1,"S",1] = grid[0,1]
    graph[0,0,"-",0][1,0,"E",1] = grid[1,0]
    for x in range(width):
        for y in range(height):
            for direction, offset in directions.items():
                nx, ny = (x + offset[0]), (y + offset[1])
                if (nx, ny) in grid:
                    cost = grid[nx, ny]
                    for steps in range(10):
                        graph[x, y, direction, steps][nx, ny, direction, steps + 1] = int(cost)
                    for other_direction in directions:
                        if other_direction != direction and not (direction in ["N", "S"] and other_direction in ["N", "S"]) and not (direction in ["E", "W"] and other_direction in ["E", "W"]):
                            for steps in range(4, 11):
                                graph[x, y, other_direction, steps][nx, ny, direction, 1] = int(cost)
    start = (0, 0, "-", 0)
    distances = dijkstra(graph, start)
    rel_keys = [k for k in distances if k[0] == width - 1 and k[1] == height - 1 and k[3] >= 4]
    print(min([distances[k] for k in rel_keys]))


def dijkstra(graph, start):
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    unvisited = []
    heapq.heappush(unvisited, (0, start))
    while unvisited:
        shortest_distance, node = heapq.heappop(unvisited)
        for neighbour in graph[node]:
            if graph[node][neighbour] != 0 and distances[neighbour] > shortest_distance + graph[node][neighbour]:
                new_distance = shortest_distance + graph[node][neighbour]
                distances[neighbour] = new_distance
                heapq.heappush(unvisited, (new_distance, neighbour))
    return distances


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
