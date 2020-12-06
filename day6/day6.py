import itertools
import functools
from typing import Callable, Iterable, List, Set

def groupLines(lines: Iterable[str]) -> List[List[str]]:
    return [list(group) for (nonempty, group) in itertools.groupby(map(str.strip, lines), lambda line: len(line) > 0) if nonempty]

def countAnswers(groups: Iterable[Iterable[str]], combine: Callable[[Set[str], Set[str]], Set[str]]) -> Iterable[Set[str]]:
    return (functools.reduce(combine, (set(m) for m in group)) for group in groups)

if __name__ == "__main__":
    with open('day6/input') as f:
        groups = groupLines(f)
        print('# Part 1')
        answers = countAnswers(groups, set.union)
        print(sum(len(a) for a in answers))

        print('#Part 2')
        answers2 = countAnswers(groups, set.intersection)
        print(sum(len(a) for a in answers2))
