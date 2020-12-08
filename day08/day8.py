import itertools
import re
from collections import defaultdict, deque
from typing import Dict, Iterable, List, NamedTuple, Set

instruction_pattern = re.compile('^(acc|jmp|nop) ([+-][0-9]+)$')
class Instruction(NamedTuple):
    op: str
    arg: int

def parse(lines: Iterable[str]) -> List[Instruction]:
    return [Instruction(match.group(1), int(match.group(2))) for line in lines if (match := instruction_pattern.match(line)) is not None]

class State(NamedTuple):
    pc: int
    acc: int

def run(program: List[Instruction]) -> Iterable[State]:
    visited: Set[int] = set()
    yield (state := State(0, 0))
    while 0 <= state.pc and state.pc < len(program):
        instruction = program[state.pc]
        if instruction.op == 'acc':
            state = State(state.pc + 1, state.acc + instruction.arg)
        elif instruction.op == 'jmp':
            state = State(state.pc + instruction.arg, state.acc)
        else:
            state = State(state.pc + 1, state.acc)
        if state.pc in visited: # loop detected
            break
        yield state
        visited.add(state.pc)

def find_terminating_indices(program: List[Instruction]) -> Set[int]:
    next_instruction = [ i + instruction.arg if instruction.op == 'jmp' else i + 1 for (i, instruction) in enumerate(program)] # execution graph
    previous_instructions: Dict[int, Set[int]] = defaultdict(set) # inverse execution graph
    for (i, j) in enumerate(next_instruction):
        previous_instructions[j].add(i)
    return set(reachable_from(len(program), previous_instructions))

def reachable_from(start: int, descendants: Dict[int, Set[int]]):
    return itertools.chain([start], *map(lambda desc: reachable_from(desc, descendants), descendants[start]))    

if __name__ == "__main__":
    with open('day08/input') as f:
        program = parse(f)

        loop_trace = list(run(program))
        print(f'Part 1: {loop_trace[-1].acc}')

        safe = find_terminating_indices(program)
        for state in loop_trace:
            instruction = program[state.pc]
            if (instruction.op == 'jmp') and (state.pc + 1) in safe:
                program[state.pc] = Instruction('nop', instruction.arg)
                break
            if (instruction.op == 'nop') and (state.pc + instruction.arg) in safe:
                program[state.pc] = Instruction('jmp', instruction.arg)
                break
        print(f'Part 2: {list(run(program))[-1].acc}')