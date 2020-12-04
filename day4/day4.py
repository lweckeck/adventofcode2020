from typing import Dict, Iterable
import re

mandatory_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }

Pass = Dict[str, str]

def parseLine(line: str) -> Pass:
    return { key: value for (key, value) in (token.split(':') for token in line.split())}

def merge(partials: Iterable[Pass]) -> Iterable[Pass]:
    current: Pass = {}
    for partial in partials:
        if len(partial) == 0 and len(current) > 0:
            yield current
            current = {}
        else:
            current.update(partial)
    if len(current) > 0:
        yield current

def valid(p: Pass) -> bool:
    fields_present = mandatory_keys.issubset(p.keys())
    fields_valid = [valid_field(k, v) for (k, v) in p.items()]
    return fields_present and all(fields_valid)

# part 2
def valid_field(key: str, value: str) -> bool:
    try:
        if key == 'byr':
            byr = int(value)
            return 1920 <= byr and byr <= 2002
        elif key == 'iyr':
            iyr = int(value)
            return 2010 <= iyr and iyr <= 2020
        elif key == 'eyr':
            iyr = int(value)
            return 2020 <= iyr and iyr <= 2030
        elif key == 'hgt':
            if value.endswith('cm'):
                cm = int(value[0:-2])
                return 150 <= cm and cm <= 193
            elif value.endswith('in'):
                inch = int(value[0:-2])
                return 59 <= inch and inch <= 76
            else:
                return False
        elif key == 'hcl':
            return re.fullmatch('#[a-f0-9]{6}', value) is not None
        elif key == 'ecl':
            return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl',  'oth'}
        elif key == 'pid':
            return re.fullmatch('[0-9]{9}', value) is not None
        elif key == 'cid':
            return True
    except: pass
    return False
# end part 2

def test(lines: Iterable[str]):
    passes = merge(map(parseLine, lines))
    count = sum(1 for p in passes if valid(p))
    print(count)

if __name__ == '__main__':
    test(open('day4/input'))