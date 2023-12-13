
def read_data():
    file = 'Days/Day13/input.txt'
    with open(file, 'r') as f:
        groups = f.read().split('\n\n')
    patterns = []
    for group in groups:
        patterns.append(list())
        for line in group.split('\n'):
            if line != '':
                patterns[-1].append(line)
    return patterns


def _get_column(array: list[str], x_column: int) -> str:
    return ''.join([line[x_column] for line in array])


def _get_mirrored_index(array: list[str]) -> int:
    for index, line in enumerate(array[:-1]):
        if line == array[index+1]:
            offset = 1
            while True:
                above_index = index - offset
                below_index = index + offset + 1
                if above_index < 0 or below_index >= len(array):
                    return index
                above = array[above_index]
                below = array[below_index]
                if above != below:
                    break
                offset += 1
    return -1


def _get_difference_count(string_a: str, string_b: str) -> int:
    count = 0
    for index in range(len(string_a)):
        if string_a[index] != string_b[index]:
            count += 1
        if count >= 2:
            break
    return count


def _get_mirrored_index_v2(array: list[str]) -> int:
    for index in range(len(array)-1):
        count = _get_difference_count(array[index], array[index+1])
        if count >= 2:
            continue
        offset = 1
        while True:
            above_index = index - offset
            below_index = index + offset + 1
            if above_index < 0 or below_index >= len(array):
                if count == 0:
                    break
                return index
            above = array[above_index]
            below = array[below_index]
            count += _get_difference_count(above, below)
            if count >= 2:
                break
            offset += 1
    return -1


def p1(patterns: list[list[str]]) -> int:
    total = 0
    for pattern in patterns:

        mirrored_index = _get_mirrored_index(pattern)
        if mirrored_index != -1:
            total += 100 * (mirrored_index + 1)
            continue

        cols = [_get_column(pattern, index)
                for index in range(len(pattern[0]))
                ]
        mirrored_index = _get_mirrored_index(cols)
        total += mirrored_index + 1

    return total


def p2(patterns: list[list[str]]) -> int:
    total = 0
    for pattern in patterns:

        mirrored_index = _get_mirrored_index_v2(pattern)
        if mirrored_index != -1:
            total += 100 * (mirrored_index + 1)
            continue

        cols = [_get_column(pattern, index)
                for index in range(len(pattern[0]))
                ]
        mirrored_index = _get_mirrored_index_v2(cols)
        total += mirrored_index + 1

    return total


def main():
    patterns = read_data()
    s1, s2 = p1(patterns), p2(patterns)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 27664
# Part 2 solution: 33991
