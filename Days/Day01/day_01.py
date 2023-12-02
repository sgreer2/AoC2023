
from re import findall, search, Match


def read_data():
    file = 'Days/Day01/input.txt'
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
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    total = 0
    pattern = r'\d|' + "|".join(numbers.keys())
    rpattern = r'\d|' + "|".join([n[::-1] for n in numbers.keys()])

    for line in lines:
        found: list[None | Match] = [None, None]
        found[0] = search(pattern, line)
        found[1] = search(rpattern, line[::-1])
        nums = ['', '']
        for index, n in enumerate(found):
            n_str = ''
            if n != None:
                n_str = n.group(0) if index == 0 else n.group(0)[::-1]
            if n_str in numbers.keys():
                nums[index] = numbers[n_str]
                continue
            nums[index] = n_str
        total += int(''.join(nums))

    return total


def main():
    lines = read_data()
    s1, s2 = p1(lines), p2(lines)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 55090
# Part 2 solution: 54845
