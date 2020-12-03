from io import TextIOWrapper
import itertools
import math

numbers = []
with open('day1/input') as f:
    numbers = [int(line) for line in f]

solutions = next(math.prod(c) for c in itertools.combinations(numbers, 2) if sum(c) == 2020)
print(solutions)

solutions2 = next(math.prod(c) for c in itertools.combinations(numbers, 3) if sum(c) == 2020)
print(solutions2)
