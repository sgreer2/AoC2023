
def read_data():
    file = 'Days/Day09/input.txt'
    with open(file, 'r') as f:
        lines = f.read().split('\n')[:-1]
    sequences = []
    for line in lines:
        sequences.append([int(num) for num in line.split()])
    return sequences


def p1(sequences: list[list[int]]) -> int:
    next_value_sum = 0

    for sequence in sequences:
        cur_sequence = sequence
        next_value = 0

        while any(cur_sequence):
            next_value += cur_sequence[-1]
            diffs = []
            for i in range(len(cur_sequence)-1):
                diffs.append(cur_sequence[i+1] - cur_sequence[i])
            cur_sequence = diffs

        next_value_sum += next_value
    return next_value_sum


def p2(sequences: list[list[int]]) -> int:
    next_value_sum = 0

    for sequence in sequences:
        cur_sequence = sequence
        firsts = []
        while any(cur_sequence):
            firsts.append(cur_sequence[0])
            diffs = []
            for i in range(len(cur_sequence)-1):
                diffs.append(cur_sequence[i+1] - cur_sequence[i])
            cur_sequence = diffs

        next_value = 0
        for num in range(len(firsts)-1, -1, -1):
            next_value = firsts[num] - next_value

        next_value_sum += next_value
    return next_value_sum


def main():
    sequences = read_data()
    s1, s2 = p1(sequences), p2(sequences)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 1884768153
# Part 2 solution: 1031
