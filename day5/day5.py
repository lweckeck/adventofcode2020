import dataclasses
import itertools
import operator

@dataclasses.dataclass()
class BoardingPass():
    row: int
    column: int
    id: int
    def __init__(self, row: int, column: int) -> None:
        (self.row, self.column) = row, column
        self.id = 8 * row + column

def bsp(seq: str, up: str) -> int:
    n = len(seq)
    return sum(2**(n-i-1) for i, c in enumerate(seq) if c == up)

def decode(line: str) -> BoardingPass:
    return BoardingPass(bsp(line[:7], 'B'), bsp(line[7:], 'R'))

# copied from https://docs.python.org/3/library/itertools.html
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

if __name__ == "__main__":
    with open('day5/input') as f:
        bps = [decode(line.strip()) for line in f]

        # Part 1
        solution1 = max(bp.id for bp in bps)
        print(solution1)

        # Part 2
        gaps = ((a, b) for a, b in pairwise(sorted(bps, key=operator.attrgetter('id'))) if (b.id - a.id) > 1)
        solution2 = next(gaps)[0].id + 1
        print(solution2)