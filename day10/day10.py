from collections import deque
from typing import Counter, List

def count_arrangements(adapters: List[int]) -> int:
    connections = deque([1], 3)
    for i in range(1, len(adapters)):
        connections.extend([0] * (adapters[i] - adapters[i-1] - 1))
        connections.append(sum(connections))
    return connections[-1]

if __name__ == "__main__":
    with open('day10/input') as f:
        adapters = sorted(map(int, f))
        adapters = [0] + adapters + [adapters[-1] + 3]

        dist = Counter(adapters[i] - adapters[i-1] for i in range(1, len(adapters)))
        print(f'Part 1: {dist[1] * dist[3]}')
        print(f'Part 2: {count_arrangements(adapters)}')