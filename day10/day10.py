from typing import Counter, List, Mapping

def distribution(adapters: List[int]) -> Mapping[int, int]:
    return Counter(adapters[i] - adapters[i-1] for i in range(1, len(adapters)))

def count_arrangements(adapters: List[int]) -> int:
    connections = [1]
    for i in range(1, len(adapters)):
        connections.append(0)
        for j in range(i-3, i):
            if j >= 0 and adapters[i] - adapters[j] <= 3:
                connections[i] += connections[j]
    return connections[-1]

if __name__ == "__main__":
    with open('day10/input') as f:
        adapters = sorted(map(int, f))
        adapters.insert(0, 0)
        adapters.append(adapters[-1] + 3)

        dist = distribution(adapters)
        print(f'Part 1: {dist[1] * dist[3]}')
        print(f'Part 2: {count_arrangements(adapters)}')