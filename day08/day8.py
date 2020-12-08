import itertools
import re
from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Dict, Iterable, List, Literal, Optional, Set, Tuple

instruction_pattern = re.compile('^(acc|jmp|nop) ([+-][0-9]+)$')
@dataclass
class Instruction:
    op: str
    arg: int

def parse(lines: Iterable[str]) -> List[Instruction]:
    return [Instruction(match.group(1), int(match.group(2))) for line in lines if (match := instruction_pattern.match(line)) is not None]

@dataclass
class State:
    pc: int
    acc: int

def run(program: List[Instruction]) -> Iterable[State]:
    yield (state := State(0, 0))
    while 0 <= state.pc and state.pc < len(program):
        instruction = program[state.pc]
        if instruction.op == 'acc':
            state = State(state.pc + 1, state.acc + instruction.arg)
        elif instruction.op == 'jmp':
            state = State(state.pc + instruction.arg, state.acc)
        else:
            state = State(state.pc + 1, state.acc)
        yield state

def noloop(trace: Iterable[State]) -> Iterable[State]:
    visited: Set[int] = set()
    for state in trace:
        if state.pc in visited:
            break
        visited.add(state.pc)
        yield state

def find_terminating_indices(program: List[Instruction]) -> Set[int]:
    next_instruction = [ i + instruction.arg if instruction.op == 'jmp' else i + 1 for (i, instruction) in enumerate(program)] # execution graph
    previous_instructions = defaultdict(set) # inverse execution graph
    for (i, j) in enumerate(next_instruction):
        previous_instructions[j].add(i)
    queue = deque([len(program)]) # last instruction + 1
    safe: Set[int] = set()
    while len(queue) > 0:
        node = queue.popleft()
        queue.extend(previous_instructions[node])
        safe.add(node)
    return safe

if __name__ == "__main__":
    with open('day08/input') as f:
        program = parse(f)

        loop_trace = list(noloop(run(program)))
        print(f'Part 1: {loop_trace[-1].acc}')

        terminating_indices = find_terminating_indices(program)
        for state in loop_trace:
            instruction = program[state.pc]
            if (instruction.op == 'jmp') and (state.pc + 1) in terminating_indices:
                instruction.op = 'nop'
                break
            if (instruction.op == 'nop') and (state.pc + instruction.arg) in terminating_indices:
                instruction.op = 'jmp'
                break
        print(f'Part 2: {list(run(program))[-1].acc}')