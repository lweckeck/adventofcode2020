import itertools
from typing import Iterable, List, Optional, Tuple
import collections
import itertools

def find_invalid(sequence: List[int], window_size: int) -> Tuple[int, int]:
    q = collections.deque(itertools.islice(sequence, window_size), window_size)
    for i, x in enumerate(sequence[window_size:]):
        if next(((a, b) for a, b in itertools.combinations(q, 2) if a + b == x), None) is None:
            return i, x
        q.append(x)
    return (-1, -1)

def find_weakness(numbers: List[int], target: int) -> int:
    i, j = next((i, j) for i, j in itertools.combinations(range(len(numbers) + 1), 2) if sum(numbers[i:j]) == target)
    return min(numbers[i:j]) + max(numbers[i:j])

def find_weakness2(numbers: List[int], target: int) -> int:
    i, j = 0, 1
    while j < len(numbers):
        if (s := sum(numbers[i:j+1])) == target:
            return min(numbers[i:j+1]) + max(numbers[i:j+1])
        elif s < target:
            j += 1
        elif s > target:
            i += 1
            if j <= i:
                j += 1
    return -1

if __name__ == "__main__":
    with open('day09/input') as f:
        numbers = list(map(int, f))
        index, invalid = find_invalid(numbers, 25)
        print(f'Part 1: {invalid}')
        print(f'Part 2: {find_weakness(numbers[:index], invalid)}')
        print(f'Part 2b: {find_weakness2(numbers[:index], invalid)}')
