import itertools
import math
from typing import Iterable, List, Tuple

def main(input: Iterable[str]):
    grid = [line.strip() for line in input]
    test1(grid)
    test2(grid)

def trees_hit(grid: List[str], slope: Tuple[int, int]) -> int:
    xs = range(0, len(grid), slope[0])
    ys = itertools.count(0, step=slope[1])

    width = len(grid[0])
    trace = [grid[x][y % width] for (x, y) in zip(xs, ys)]
    return trace.count('#')

def test1(grid: List[str]):
    print(trees_hit(grid, (1, 3)))

def test2(grid: List[str]):
    slopes = [(1, 1), (1,3), (1,5), (1,7), (2,1)]
    trees = [trees_hit(grid, slope) for slope in slopes]
    result = math.prod(trees)
    print(result)

if __name__ == '__main__':
    path = 'day3/testinput'
    path = 'day3/input'
    with open(path) as f:
        main(f)