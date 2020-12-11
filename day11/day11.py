import itertools

from collections import defaultdict
from typing import Dict, Iterable, List, Mapping, Text, Tuple

Index = Tuple[int, int]
Grid = List[List[str]]
def compute_neighbours(grid: Grid, maxdistance: int = None) -> Dict[Index, List[Index]]:
    directions = [(di, dj) for di in [-1, 0, 1] for dj in [-1, 0, 1] if di != 0 or dj != 0]
    result: Dict[Index, List[Index]] = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                continue
            for (di, dj) in directions:
                ray = ((i + d*di, j + d*dj) for d in (range(1, maxdistance+1) if maxdistance else itertools.count(1)))
                for (ii, jj) in ray:
                    if ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[i]):
                        break
                    if grid[ii][jj] != '.':
                        result[(i,j)].append((ii, jj))
                        break
    return result

def step(grid: Grid, neighbors: Mapping[Index, List[Index]], threshold: int) -> bool:
    updates: List[Tuple[Index, str]] = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbor_seats = [grid[ii][jj] for (ii, jj) in neighbors[(i, j)]]
            if grid[i][j] == 'L' and neighbor_seats.count('#') == 0:
                updates.append(((i, j), '#'))
            elif grid[i][j] == '#' and neighbor_seats.count('#') >= threshold:
                updates.append(((i, j), 'L'))
    for ((i, j), c) in updates:
        grid[i][j] = c
    return len(updates) > 0

if __name__ == "__main__":
    with open('day11/input') as f:
        grid = [list(line.strip()) for line in f]
        grid2 = [row[:] for row in grid] # copy

        neighbors1 = compute_neighbours(grid, maxdistance=1)
        while step(grid, neighbors1, 4): pass
        print(f'Part 1: {sum(line.count("#") for line in grid)}')

        neighbors2 = compute_neighbours(grid2)
        while step(grid2, neighbors2, 5): pass
        print(f'Part 2: {sum(line.count("#") for line in grid2)}')
