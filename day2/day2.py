import re
import functools as ft
from typing import Generator, Optional, Tuple, Iterable

pattern = re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")

def parse(lines: Iterable[str]) -> Iterable[Tuple[int, int, str, str]]:
    for line in lines:
        match = pattern.match(line)
        if match is not None:
            yield (int(match.group(1)), int(match.group(2)), match.group(3), match.group(4))

# rule 1
def valid(lower: int, upper: int, char: str, pw:str ) -> bool:
    count = pw.count(char)
    return  lower <= count and count <= upper

with open('day2/input') as f:
    c = sum(1 for t in parse(f) if valid(*t))
    print(c)

# rule 2

def valid2(left: int, right: int, char: str, pw: str) -> bool:
    return sum(map(int, [pw[left-1] == char, pw[right-1] == char])) == 1

with open('day2/input') as f:
    c = sum(1 for t in parse(f) if valid2(*t))
    print(c)
