import sys
import itertools
import math

lines = []
with open('day1/input') as f:
    lines = f.readlines()

numbers = [int(line.strip()) for line in lines]

# for i in range(len(numbers)):
#     a = numbers[i]
#     for j in range(i + 1, len(numbers)):
#         b = numbers[j]
#         if a + b == 2020:
#             print(a * b)

solutions = next(math.prod(c) for c in itertools.combinations(numbers, 2) if sum(c) == 2020)
print(solutions)

# for i in range(len(numbers)):
#     a = numbers[i]
#     for j in range(i + 1, len(numbers)):
#         b = numbers[j]
#         for k in range(j+1, len(numbers)):
#             c = numbers[k]
#             if sum([a, b, c]) == 2020:
#                 print(a * b * c)

solutions = next(math.prod(c) for c in itertools.combinations(numbers, 3) if sum(c) == 2020)
print(solutions)
