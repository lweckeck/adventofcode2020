import itertools
from typing import Dict, Iterable, List, TypeVar

def play(starting_numbers: List[int]) -> Iterable[int]:
    last_turn: Dict[int, int] = dict()
    for turn, number in enumerate(starting_numbers):
        yield number
        last_turn[number] = turn
    yield (number := 0) # input numbers are unique; last number was called first
    for turn in itertools.count(len(starting_numbers)):
        previous = number
        yield (number := turn - last_turn[number] if number in last_turn else 0)
        last_turn[previous] = turn

_T = TypeVar('_T')
def nth(iter: Iterable[_T], n: int, default: _T = None): return next(itertools.islice(iter, n, None), default)

if __name__ == "__main__":
    input = [int(t) for t in '1,20,11,6,12,0'.split(',')]
    print(f'Part 1: {nth(play(input), 2020 - 1)}')
    print(f'Part 2: {nth(play(input), 30000000 - 1)}')
