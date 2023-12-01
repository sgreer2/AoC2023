
from re import findall
from math import inf


def read_data():
    file = 'Day01/t_input.txt' if TESTING else 'Day01/input.txt'
    with open(file, 'r') as f:
        return f.read().split('\n')[:-1]


def p1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        nums = findall(r'\d', line)
        val = int(''.join([nums[0], nums[-1]]))
        total += val

    return total


def p2(lines: list[str]) -> int:
    numbers = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    total = 0

    for line in lines:
        lowest = [inf, '']
        highest = [-inf, '']
        for k, v in numbers.items():
            if k in line:
                index = line.index(k)
                rindex = line.rindex(k)
                if index < lowest[0]:
                    lowest = [index, k]
                if rindex > highest[0]:
                    highest = [rindex, k]

            if v in line:
                index = line.index(v)
                rindex = line.rindex(v)
                if index < lowest[0]:
                    lowest = [index, k]
                if rindex > highest[0]:
                    highest = [rindex, k]

        val = ''.join([lowest[1], highest[1]])
        total += int(val)

    return total


def main():
    lines = read_data()
    s1, s2 = p1(lines), p2(lines)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


TESTING = False

if __name__ == '__main__':
    main()

# Part 1 solution: 55090
# Part 2 solution: 54845
