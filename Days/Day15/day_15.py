
def read_data():
    file = 'Days/Day15/input.txt'
    with open(file, 'r') as f:
        return f.read().split('\n')[0]


def string_to_hash(string: str) -> int:
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value = value % 256

    return value


def p1(data: str) -> int:
    total = 0
    for line in data.split(','):
        total += string_to_hash(line)
    return total


def p2(data) -> int:
    return -1


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 519603
# Part 2 solution:
