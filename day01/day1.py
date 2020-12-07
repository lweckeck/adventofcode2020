from io import TextIOWrapper
import itertools
import math

numbers = []
with open('day1/input') as f:
    numbers = [int(line) for line in f]

print("# Part 1")
if solution := next((math.prod(c) for c in itertools.combinations(numbers, 2) if sum(c) == 2020), None):
    print(solution)
else:
    print('No solution found!')

print('# Part 2')
if solution := next((math.prod(c) for c in itertools.combinations(numbers, 3) if sum(c) == 2020), None):
    print(solution)
else:
    print('No solution found!')