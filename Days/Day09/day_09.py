
def read_data():
    file = 'Days/Day09/input.txt'
    with open(file, 'r') as f:
        lines = f.read().split('\n')[:-1]
    sequences = []
    for line in lines:
        sequences.append([int(num) for num in line.split()])
    return sequences


def _allZeroes(array: list[int]) -> bool:
    for num in array:
        if num != 0:
            return False
    return True


def p1(sequences: list[list[int]]) -> int:
    next_value_sum = 0

    for sequence in sequences:
        history = [sequence]
        while True:
            if _allZeroes(history[-1]):
                break
            diffs = []
            for i in range(len(history[-1])-1):
                diffs.append(history[-1][i+1] - history[-1][i])
            history.append(diffs)

        next_value = 0
        for line in history:
            next_value += line[-1]
        next_value_sum += next_value
    return next_value_sum


def p2(sequences: list[list[int]]) -> int:
    next_value_sum = 0

    for sequence in sequences:
        history = [sequence]
        while True:
            if _allZeroes(history[-1]):
                break
            diffs = []
            for i in range(len(history[-1])-1):
                diffs.append(history[-1][i+1] - history[-1][i])
            history.append(diffs)

        next_value = 0
        for h_index in range(len(history)-1, 0, -1):
            next_value = history[h_index-1][0] - next_value
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
