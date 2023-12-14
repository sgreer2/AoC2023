from enum import IntEnum
from functools import cache


def read_data():
    file = 'Days/Day14/input.txt'
    with open(file, 'r') as f:
        return tuple(f.read().split('\n')[:-1])


class Direction(IntEnum):
    North = 1
    East = 2
    South = 3
    West = 4


@cache
def _get_weight(array: tuple[str, ...]) -> int:
    total = 0
    cur_val = len(array)
    for line in array:
        for char in line:
            if char == 'O':
                total += cur_val
        cur_val -= 1
    return total


@cache
def _tilt_row(string: str) -> str:
    row = list(string)
    last_occupied = -1
    for char_index in range(len(row)):
        cur_char = row[char_index]
        if cur_char == '#':
            last_occupied = char_index
            continue
        if cur_char == 'O':
            row[char_index] = '.'
            row[last_occupied+1] = 'O'
            last_occupied += 1
    return ''.join(row)


@cache
def _tilt_array(array: tuple[str, ...], direction: Direction = Direction.North) -> tuple[str, ...]:
    new_array = []
    for i in range(len(array)):
        new_array.append(list(array[i]))
    if direction == Direction.North or direction == Direction.South:
        for col_index in range(len(array[0])):
            cur_col = ''.join([line[col_index] for line in array])
            new_col = ''
            if direction == Direction.North:
                new_col = _tilt_row(cur_col)
            else:
                new_col = _tilt_row(cur_col[::-1])
                new_col = new_col[::-1]

            for i, c in enumerate(new_col):
                new_array[i][col_index] = c
    else:
        for row_index in range(len(array)):
            cur_row = ''.join(array[row_index])
            new_row = ''
            if direction == Direction.West:
                new_row = _tilt_row(cur_row)
            else:
                new_row = _tilt_row(cur_row[::-1])
                new_row = new_row[::-1]
            for i, c in enumerate(new_row):
                new_array[row_index][i] = c

    temp_arr = []
    for line in new_array:
        temp_arr.append(''.join(line))
    return tuple(temp_arr)


def p1(data: tuple[str, ...]) -> int:
    return _get_weight(_tilt_array(data))


def p2(data: tuple[str, ...]) -> int:
    cycles = 1_000_000_000
    visited = []
    pattern = []

    for _ in range(cycles):
        data = _tilt_array(data, Direction.North)
        data = _tilt_array(data, Direction.West)
        data = _tilt_array(data, Direction.South)
        data = _tilt_array(data, Direction.East)

        weight = _get_weight(data)
        if weight in visited:
            if weight in pattern and len(pattern) > 5:
                break
            pattern.append(weight)
        else:
            visited.extend(pattern)
            visited.append(weight)
            pattern = []
    initial_len = len(visited) - len(pattern)
    index = (cycles - initial_len) % len(pattern)-1
    return pattern[index]


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 110128
# Part 2 solution: 103861
