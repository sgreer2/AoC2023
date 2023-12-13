
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
    mirror_index = -1
    offset = 0
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

    return mirror_index


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
    return -1


def main():
    patterns = read_data()
    s1, s2 = p1(patterns), p2(patterns)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 27664
# Part 2 solution:
