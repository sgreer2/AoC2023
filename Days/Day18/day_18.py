from enum import Enum
from math import floor


def read_data():
    file = 'Days/Day18/input.txt'
    with open(file, 'r') as f:
        return [Instruction(line) for line in f.read().split('\n')[:-1]]


class D(Enum):
    North = (0, -1)
    South = (0, 1)
    East = (1, 0)
    West = (-1, 0)


class Instruction:
    direction: D
    value: int
    direction_p2: D
    value_p2: int

    def __init__(self, data: str) -> None:
        d, v, s = data.split(' ')
        direction = D.North
        match d:
            case 'U':
                direction = D.North
            case 'R':
                direction = D.East
            case 'D':
                direction = D.South
            case 'L':
                direction = D.West

        self.direction = direction
        self.value = int(v)

        d = s[-2]
        match d:
            case '3':
                direction = D.North
            case '0':
                direction = D.East
            case '1':
                direction = D.South
            case '2':
                direction = D.West

        self.direction_p2 = direction
        self.value_p2 = int(s[2:-2], 16)

    def get_data(self, part_2: bool = False) -> tuple[D, int]:
        if part_2:
            return (self.direction_p2, self.value_p2)
        return (self.direction, self.value)


def _solve(instructions: list[Instruction], part_2: bool = False) -> int:
    area = 0
    coord = [0, 0]
    perimiter = 0
    for inst in instructions:
        direction, length = inst.get_data(part_2)
        perimiter += length
        coord[0] += direction.value[0] * length
        coord[1] += direction.value[1] * length
        if direction == D.North:
            area -= (length * coord[0])
            continue
        if direction == D.South:
            area += (length * coord[0])
    return int(area + floor(perimiter/2) + 1)


def p1(instructions: list[Instruction]) -> int:
    return _solve(instructions)


def p2(instructions: list[Instruction]) -> int:
    return _solve(instructions, True)


def main():
    instructions = read_data()
    s1, s2 = p1(instructions), p2(instructions)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 56678
# Part 2 solution: 79088855654037
