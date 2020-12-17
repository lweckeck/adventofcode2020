from typing import List, NamedTuple, Set, Tuple
import math

class Rule(NamedTuple):
    label: str
    intervals: List[Tuple[int, int]]
    def match(self, field: int) -> bool: return any(interval[0] <= field and field <= interval[1] for interval in self.intervals)
    
def parseRule(line: str) -> Rule:
    label, spec = line.split(': ')
    intervals = [(int(interval[0]), int(interval[1])) for interval in (interval.split('-') for interval in spec.split(' or '))]
    return Rule(label, intervals)

if __name__ == "__main__":
    with open('day16/input') as f:
        input_blocks = f.read().split('\n\n')
        rules = [parseRule(line) for line in input_blocks[0].splitlines()]
        ticket = [int(field) for field in input_blocks[1].splitlines()[1].split(',')]
        others = [[int(field) for field in line.split(',')] for line in input_blocks[2].splitlines()[1:]]

        invalid = [field for ticket in others for field in ticket if not any(rule.match(field) for rule in rules)]
        print(f'Part 1: {sum(invalid)}')

        valid = [ticket] + [ticket for ticket in others if not any(field in invalid for field in ticket)]

        matching_rules = [(i, {rule.label for rule in rules if all(rule.match(field) for field in (ticket[i] for ticket in valid))}) for i in range(len(ticket))]
        assigned: Set[str] = set() 
        field_mapping: List[str] = ['' for _ in ticket]       
        for (i, matching) in sorted(matching_rules, key=lambda x: len(x[1])):
            unassigned = matching - assigned
            assert(len(unassigned) == 1)
            field_mapping[i] = next(iter(unassigned))
            assigned.update(unassigned)
        assert(all(field != '' for field in field_mapping))
        assert(len(field_mapping) == len(set(field_mapping)))
        departure_fields = [i for (i, field) in enumerate(field_mapping) if field.startswith('departure')]
        assert(len(departure_fields) == 6)

        print(f'Part 2: {math.prod(ticket[i] for i in departure_fields)}')