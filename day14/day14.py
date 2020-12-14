from typing import Dict, List

def run1(program: List[str]) -> Dict[int, int]:
    ones = 0x0
    zeros = 0xFFFF
    mem: Dict[int, int] = dict()
    for line in program:
        ins, arg = line.split(' = ')
        if ins == 'mask':
            ones = sum(1 << i for (i, c) in enumerate(reversed(arg)) if c == '1')
            zeros =sum(1 << i for (i, c) in enumerate(reversed(arg)) if c != '0')
        else:
            addr = int(ins[4:-1])
            mem[addr] = (int(arg) & zeros) | ones
    return mem

def expand_addr(addr: int, floating: List[int]) -> List[int]:
    return [addr] if len(floating) == 0 else expand_addr(addr | floating[0], floating[1:]) + expand_addr(addr & ~floating[0], floating[1:])

def run2(program: List[str]) -> Dict[int, int]:
    ones = 0x0
    xes: List[int] = []
    mem: Dict[int, int] = dict()
    for line in program:
        ins, arg = line.split(' = ')
        if ins == 'mask':
            ones = sum(1 << i for (i, c) in enumerate(reversed(arg)) if c == '1')
            xes = [1 << i for (i, x) in enumerate(reversed(arg)) if x == 'X']
        else:
            addr = int(ins[4:-1])
            for eaddr in expand_addr(addr | ones, xes):
                mem[eaddr] = int(arg)
    return mem

if __name__ == "__main__":
    with open('day14/input') as f:
        lines = [l.strip() for l in f]
        r = run1(lines)
        print(f'Part 1: {sum(r.values())}')
        r2 = run2(lines)
        print(f'Part 2: {sum(r2.values())}')
