import itertools
import math

if __name__ == "__main__":
    with open('day13/input') as f:
        earliest_departure = int(f.readline())
        schedule = [(index, int(interval)) for (index, interval) in enumerate(f.readline().strip().split(',')) if interval != 'x']

        next_departure = min(((interval - (earliest_departure % interval), interval) for (_, interval) in schedule), key=lambda p: p[0])
        print(f'Part 1: {math.prod(next_departure)}')

        # Approach: Chinese remainder theorem sieve
        # (a, n) s.t. x % n == a, where x is the contest solution
        constraints = [((interval - offset) % interval, interval) for (offset, interval) in sorted(schedule, key=lambda p: p[1], reverse=True)]
        offset, interval = constraints[0]
        for next_offset, next_interval in constraints[1:]:
            offset = next(x for x in itertools.count(offset, interval) if x % next_interval == next_offset)
            interval = interval * next_interval // math.gcd(interval, next_interval) # could be omitted since intervals seem to be pairwise coprimes
        print(f'Part 2: {offset}')
