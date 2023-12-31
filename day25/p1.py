"""
Step 1: guess a solution
Step 2: check if it is correct
Step 3: It is.
Step 4: ...but only for larger graphs.
"""
from pathlib import Path
from collections import defaultdict, Counter
import heapq


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def check_partitions(graph, rem_edges):
    partitions = []
    unpartitioned = set(graph.keys())
    while unpartitioned:
        node = unpartitioned.pop()
        partition = {node}
        partitions.append(partition)
        new_nodes = {node}
        while new_nodes:
            expand, new_nodes = new_nodes, set()
            for n1 in expand:
                for n2 in graph[n1]:
                    if n2 in unpartitioned and (n1, n2) not in rem_edges and (n2, n1) not in rem_edges:
                        partition.add(n2)
                        new_nodes.add(n2)
                        unpartitioned.remove(n2)
    return partitions


def solve(lines: list[str]):
    graph = defaultdict(lambda: defaultdict(lambda: False))
    edges = set()
    for line in lines:
        n1, right = line.split(": ", 1)
        for n2 in right.split(" "):
            graph[n1][n2] = True
            graph[n2][n1] = True
            edges.add((n1, n2))
            edges.discard((n2, n1))
    counter = Counter()
    for line in lines:
        predecessors, distances = dijkstra(graph, line[:3])
        for n1, n2 in predecessors.items():
            counter[tuple(sorted((n1, n2)))] += 1
    partitions = check_partitions(graph, [edge for edge, freq in counter.most_common(3)])
    print([len(p) for p in partitions])


def dijkstra(graph, start):
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    unvisited = []
    predecessors = {}
    heapq.heappush(unvisited, (0, start))
    while unvisited:
        shortest_distance, node = heapq.heappop(unvisited)
        for neighbour in graph[node]:
            if graph[node][neighbour] != 0 and distances[neighbour] > shortest_distance + graph[node][neighbour]:
                new_distance = shortest_distance + graph[node][neighbour]
                distances[neighbour] = new_distance
                predecessors[neighbour] = node
                heapq.heappush(unvisited, (new_distance, neighbour))
    return predecessors, distances


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
