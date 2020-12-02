import sys
import itertools
import math
import re

pattern = re.compile("(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<char>[a-z]): (?P<pw>[a-z]+)")

# rule 1
valid = 0
with open('day2/input') as f:
    for line in f:
        match = pattern.match(line)
        if match is None:
            print(f'Invalid format: {line}', sys.stderr)
            continue
        pw = match.group('pw')
        char = match.group('char')
        minc = int(match.group('min'))
        maxc = int(match.group('max'))
        count = pw.count(char)
        if minc <= count and count <= maxc:
            valid += 1

print(valid)

# rule 2
valid = 0
with open('day2/input') as f:
    for line in f:
        match = pattern.match(line)
        if match is None:
            print(f'Invalid format: {line}', sys.stderr)
            continue
        pw = match.group('pw')
        char = match.group('char')
        p1 = int(match.group('min'))
        p2 = int(match.group('max'))
        if sum(map(int, [pw[p1-1] == char, pw[p2-1] == char])) == 1:
            valid += 1

print(valid)