from matplotlib.path import Path
from enum import Enum


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
    string: str

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
        self.string = s[1:-1]

    def get_locs(self, start: tuple[int, int]) -> list[tuple[int, int]]:
        x, y = start
        offset = self.direction.value
        array: list[tuple[int, int]] = []
        for _ in range(self.value):
            x += offset[0]
            y += offset[1]
            array.append((x, y))
        return array

    def __str__(self) -> str:
        return f'{self.direction}, {self.value}, {self.string}'


def p1(instructions: list[Instruction]) -> int:
    start = (0, 0)
    locations: list[tuple[int, int]] = [start]
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0
    for inst in instructions:
        cur_loc = locations[-1]
        locs = inst.get_locs(cur_loc)
        for loc in locs:
            min_x = min(min_x, loc[0])
            max_x = max(max_x, loc[0])
            min_y = min(min_y, loc[1])
            max_y = max(max_y, loc[1])
            locations.append(loc)
    path = Path(locations)
    count = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            point = (x, y)
            if point in locations:
                count += 1
                continue
            if path.contains_point(point):
                count += 1
    return count


def p2(instructions: list[Instruction]) -> int:
    return -1


def main():
    instructions = read_data()
    s1, s2 = p1(instructions), p2(instructions)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution:
# Part 2 solution:
