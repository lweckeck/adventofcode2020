import collections
import re
from typing import Dict, Iterable

Rules = Dict[str, Dict[str, int]]

rule_pattern = re.compile('^(\w+ \w+) bags contain (no other bags|([0-9]+ \w+ \w+ bags?(, )?)+).$')
right_side_pattern = re.compile('([0-9]+) (\w+ \w+) bags?')
def parse(lines: Iterable[str]) -> Rules:
    return { rule.group(1): {right_side.group(2): int(right_side.group(1)) 
            for right_side in right_side_pattern.finditer(rule.group(2))}
            for line in lines if (rule := rule_pattern.match(line)) is not None}

def bags_for(target: str, rules: Rules) -> Iterable[str]:
    queue = collections.deque([target])
    while len(queue) > 0:
        yield (item := queue.popleft())
        queue.extend(colour for (colour, contents) in rules.items() if item in contents)

def bags_in(target: str, rules: Rules) -> int:
    return 1 + sum(rules[target][descendant] * bags_in(descendant, rules) for descendant in rules[target])

if __name__ == "__main__":
    with open('day07/input') as f:
        rules = parse(f)
        print(f'Part 1: {len(set(bags_for("shiny gold", rules))) - 1}')
        print(f'Part 2: {bags_in("shiny gold", rules) - 1}')