from typing import Iterable, Tuple

Vec = Tuple[int, int]
def vadd(v1: Vec, v2: Vec) -> Vec: return (v1[0] + v2[0], v1[1] + v2[1])

def cardir(dir: str, val: int) -> Vec: return {'N': (0, val), 'S': (0, -val), 'E': (val, 0), 'W': (-val, 0)}[dir]
def carsin(degrees: int) -> int: return [0, 1, 0, -1][int(degrees/90) % 4]
def carcos(degrees: int) -> int: return carsin(degrees + 90)

Instruction = Tuple[str, int]
def navigate(instructions: Iterable[Instruction], wp_mode: bool = False) -> Vec:
    pos = (0, 0)
    wp = (10, 1) if wp_mode else (1, 0)
    for nav, val in instructions:
        if nav in 'NSEW' and wp_mode:
            wp = vadd(wp, cardir(nav, val))
        elif nav in 'NSEW' and not wp_mode:
            pos = vadd(pos, cardir(nav, val))
        elif nav in 'LR':
            deg = val if nav == 'L' else -val
            wp = (carcos(deg)*wp[0] - carsin(deg)*wp[1], carsin(deg)*wp[0] + carcos(deg)*wp[1])
        elif nav == 'F':
            pos = (pos[0] + val * wp[0], pos[1] + val * wp[1])
    return pos

if __name__ == "__main__":
    with open('day12/input') as f:
        navs = [(line[0], int(line[1:])) for line in f]
        pos1 = navigate(navs, wp_mode=False)
        print(f'Part 1: {abs(pos1[0] + abs(pos1[1]))}')

        pos2 = navigate(navs, wp_mode=True)
        print(f'Part 2: {abs(pos2[0] + abs(pos2[1]))}')