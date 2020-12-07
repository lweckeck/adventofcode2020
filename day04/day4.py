import itertools
from typing import Dict, Iterable
import re

Pass = Dict[str, str]

def parse(lines: Iterable[str]) -> Iterable[Pass]:
    for (nonempty, group) in itertools.groupby((line.strip() for line in lines), lambda l: len(l) > 0):
        if nonempty:
            tokens = [token.split(':', 2) for tokens in (line.split() for line in group) for token in tokens]
            yield {key: value for (key, value) in tokens}

mandatory_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }
def valid(p: Pass) -> bool:
    return mandatory_keys.issubset(p.keys())

def valid2(p: Pass) -> bool:
    fields_present = valid(p)
    fields_valid = [valid_field(k, v) for (k, v) in p.items()]
    return fields_present and all(fields_valid)

def valid_field(key: str, value: str) -> bool:
    if key == 'byr' and value.isdigit():
        return 1920 <= (byr := int(value)) and byr <= 2002
    elif key == 'iyr' and value.isdigit():
        return 2010 <= (iyr := int(value)) and iyr <= 2020
    elif key == 'eyr' and value.isdigit():
        return 2020 <= (iyr := int(value)) and iyr <= 2030
    elif key == 'hgt' and (match := re.fullmatch('([0-9]+)(cm|in)', value)):
        height, unit = int(match.group(1)), match.group(2)
        return (150 <= height and height <= 193) if unit == 'cm' else (59 <= height and height <= 76)
    elif key == 'hcl':
        return re.fullmatch('#[a-f0-9]{6}', value) is not None
    elif key == 'ecl':
        return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl',  'oth'}
    elif key == 'pid':
        return re.fullmatch('[0-9]{9}', value) is not None
    elif key == 'cid':
        return True
    return False

if __name__ == '__main__':
    with open('day4/input') as f:
        passes = list(parse(f))
        print('Part 1')
        print(sum(1 for p in passes if valid(p)))

        print('Part 2')
        print(sum(1 for p in passes if valid2(p)))