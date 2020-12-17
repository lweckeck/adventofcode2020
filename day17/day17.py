import itertools
import functools
from typing import Set, Tuple

P = Tuple[int, ...]
@functools.lru_cache
def neighbors(p: P) -> Set[P]:
    return {tuple(pi + di for (pi, di) in zip(p, d)) for d in itertools.product([-1, 0, 1], repeat=len(p))} - {p}

def simulate(grid: Set[P], cycles: int) -> Set[P]:
    for _ in range(cycles):
        deactivate: Set[P] = set()
        could_activate: Set[P] = set()
        activate: Set[P] = set()
        for p in grid:
            ns = neighbors(p)
            could_activate.update(ns)
            if len(ns & grid) not in [2, 3]:
                deactivate.add(p)
        for c in could_activate - grid:
            if len(neighbors(c) & grid) == 3:
                activate.add(c)
        grid.update(activate)
        grid.difference_update(deactivate)
    return grid

if __name__ == "__main__":
    with open('day17/input') as f:
        grid3: Set[P] = set()
        grid4: Set[P] = set()
        for (y, row) in enumerate(f.read().splitlines()):
            for (x, cell) in enumerate(row):
                if cell == '#':
                    grid3.add((x, y, 0))
                    grid4.add((x, y, 0, 0))
        print(f'Part 1: {len(simulate(grid3, 6))}')
        print(f'Part 2: {len(simulate(grid4, 6))}')