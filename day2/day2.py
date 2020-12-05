import re
import functools as ft
from typing import Generator, Optional, Tuple, Iterable, Union

Input = Tuple[int, int, str, str]

pattern = re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")
def parse(line: str) -> Optional[Input]:
    if (match := pattern.match(line)) is not None:
        return (int(match.group(1)), int(match.group(2)), match.group(3), match.group(4))
    else:
        return None

def valid(lower: int, upper: int, char: str, pw:str ) -> bool:
    return  lower <= (count := pw.count(char)) and count <= upper

def valid2(left: int, right: int, char: str, pw: str) -> bool:
    return sum(map(int, [pw[left-1] == char, pw[right-1] == char])) == 1

if __name__ == "__main__":
    with open('day2/input') as f:
        inputs = [parsed for line in f if (parsed := parse(line)) is not None]

        print("# Part 1")
        print(sum(1 for i in inputs if valid(*i)))

        print('# Part 2')
        print(sum (1 for i in inputs if valid2(*i)))