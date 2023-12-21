from enum import Enum


def read_data():
    file = 'Days/Day21/input.txt'
    with open(file, 'r') as f:
        return f.read().split('\n')[:-1]


class D(Enum):
    North = (0, -1)
    East = (1, 0)
    South = (0, 1)
    West = (-1, 0)


def p1(plot: list[str], step_limit: int = 64) -> int:
    rocks: dict[tuple[int, int], bool] = dict()
    stepped_locations: set[tuple[int, int]] = set()
    for y, line in enumerate(plot):
        for x in range(len(line)):
            if line[x] == '.':
                continue
            if line[x] == '#':
                rocks[(x, y)] = True
                continue
            stepped_locations.add((x, y))

    for _ in range(step_limit):
        new_stepped_locations: set[tuple[int, int]] = set()
        for x, y in stepped_locations:
            for dir in D:
                n_x, n_y = dir.value
                new_pos = (x+n_x, y+n_y)
                if new_pos in rocks:
                    continue
                if new_pos not in new_stepped_locations:
                    new_stepped_locations.add(new_pos)
        stepped_locations = new_stepped_locations
    return len(stepped_locations)


def p2(data) -> int:
    return -1


def main():
    plot = read_data()
    s1, s2 = p1(plot), p2(plot)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 3746
# Part 2 solution:
