from enum import IntEnum


def read_data():
    file = 'Days/Day14/input.txt'
    with open(file, 'r') as f:
        return f.read().split('\n')[:-1]


class Direction(IntEnum):
    North = 1
    East = 2
    South = 3
    West = 4


def _get_weight(array: list[str]) -> int:
    total = 0
    cur_val = len(array)
    for line in array:
        for char in line:
            if char == 'O':
                total += cur_val
        cur_val -= 1
    return total


def _tilt(array: list[str], direction: Direction = Direction.North) -> list[str]:
    new_array = []
    for i in range(len(array)):
        new_array.append(list(array[i]))
    if direction == Direction.North:
        for col_index in range(len(array[0])):
            cur_col = [line[col_index] for line in array]
            for char_index in range(1, len(cur_col)):
                cur_index = char_index
                while True:
                    if cur_index <= 0:
                        break
                    if cur_col[cur_index] in ['#', '.']:
                        break
                    if cur_col[cur_index-1] == '.':
                        cur_col[cur_index-1] = 'O'
                        cur_col[cur_index] = '.'
                    cur_index -= 1
            for i, c in enumerate(cur_col):
                new_array[i][col_index] = c
    return new_array


def p1(data: list[str]) -> int:
    return _get_weight(_tilt(data))


def p2(data: list[str]) -> int:
    return -1


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution:
# Part 2 solution:
