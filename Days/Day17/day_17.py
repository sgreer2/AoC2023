from __future__ import annotations
from enum import Enum
from queue import PriorityQueue


def read_data():
    file = 'Days/Day17/input.txt'
    with open(file, 'r') as f:
        return [[int(num)for num in line]for line in f.read().split('\n')[:-1]]


class D(Enum):
    Empty = (0, 0)
    North = (0, -1)
    East = (1, 0)
    South = (0, 1)
    West = (-1, 0)


class Pos:
    value: int
    x: int
    y: int
    steps: int
    direction: D

    def __init__(self, value: int, pos: tuple[int, int], direction: D = D.Empty, steps: int = 0) -> None:
        self.value = value
        self.x = pos[0]
        self.y = pos[1]
        self.direction = direction
        self.steps = steps

    def get_pos(self) -> tuple[int, int]:
        return (self.x, self.y)

    def get_data(self):
        return (self.x, self.y, self.direction, self.steps)

    def __lt__(self, other: Pos) -> bool:
        if self.value == other.value:
            if self.x == other.x:
                if self.y == other.y:
                    if self.direction == other.direction:
                        return self.steps < other.steps
                    return True
                return self.y < other.y
            return self.x < other.x
        return self.value < other.value


def p1(heat_map: list[list[int]]) -> int:
    start = (0, 0)
    _map_size = len(heat_map) - 1
    end = (_map_size, _map_size)
    max_steps = 3
    visited: set[tuple[int, int, D, int]] = set()
    queue: PriorityQueue[Pos] = PriorityQueue()
    queue.put(Pos(0, start))

    while queue:
        current: Pos = queue.get()

        if current.get_pos() == end:
            return current.value

        if current.get_data() in visited:
            continue
        visited.add(current.get_data())

        cur_x, cur_y = current.get_pos()
        for direction in D:
            if direction == D.Empty:
                continue

            # Check bounds of new positions
            new_x = cur_x + direction.value[0]
            new_y = cur_y + direction.value[1]
            if new_x < 0 or new_x > _map_size:
                continue
            if new_y < 0 or new_y > _map_size:
                continue

            # Check number of steps
            new_steps = current.steps
            if direction == current.direction:
                new_steps += 1
            else:
                new_steps = 1
            if new_steps > max_steps:
                continue
            new_value = current.value + heat_map[new_y][new_x]
            queue.put(Pos(new_value, (new_x, new_y), direction, new_steps))

    return -1


def p2(data) -> int:
    return -1


def main():
    heat_map = read_data()
    s1, s2 = p1(heat_map), p2(heat_map)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 1195
# Part 2 solution:
