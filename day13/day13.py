import itertools
import math

if __name__ == "__main__":
    with open('day13/input') as f:
        earliest_departure = int(f.readline())
        schedule = [(int(id) if id.isdigit() else 0) for id in f.readline().strip().split(',')]
        next_departure, id = next((departure, id) for departure in itertools.count(earliest_departure) for id in schedule if id > 0 if departure % id == 0)
        print(f'Part 1: {(next_departure - earliest_departure) * id}')

        # (a, n) s.t. x % n == a, where x is the contest solution
        constraints = [((interval - offset) % interval, interval) for (offset, interval) in enumerate(schedule) if interval != 0]
        sorted_constraints = sorted(constraints, key=lambda p: p[1], reverse=True) # begin with larger intervals
        offset, interval = sorted_constraints[0]
        x = 0
        for next_offset, next_interval in sorted_constraints[1:]:
            x = next(x for x in itertools.count(offset, interval) if x % next_interval == next_offset)
            offset = x # start with next x, eventual solution cannot be smaller
            interval = interval * next_interval // math.gcd(interval, next_interval)
        print(f'Part 2: {x}')
