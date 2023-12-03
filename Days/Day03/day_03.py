from re import finditer


def read_data():
    file = 'Days/Day03/input.txt'
    with open(file, 'r') as f:
        return parse(f.read().split('\n')[:-1])


def parse(array: list[str]) -> tuple[dict, dict]:
    num_locs = dict()
    sym_locs = dict()
    for y, line in enumerate(array):

        nums = finditer(r'\d+', line)
        for num in nums:
            num_locs[(y, num.span())] = int(num.group(0))

        for x, c in enumerate(list(line)):
            invalid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
            if c not in invalid:
                sym_locs[(y, x)] = c

    return (num_locs, sym_locs)


def compare(num: tuple[int, tuple[int, int]], sym: tuple[int, int]) -> bool:
    s_y, s_x = sym
    n_y = num[0]
    n_x = num[1]
    if s_y > n_y+1 or s_y < n_y-1:  # If the Y pos is outside valid range
        return False

    if s_x < n_x[0]-1 or s_x > n_x[1]:  # If outside X range
        return False

    return True


def p1(data: tuple[dict, dict]) -> int:
    num_dict, sym_dict = data
    total = 0
    for n_loc, num in num_dict.items():
        for s_loc, s in sym_dict.items():
            if compare(n_loc, s_loc):
                total += num
                break

    return total


def p2(data: tuple[dict, dict]) -> int:
    num_dict, sym_dict = data
    total = 0
    for s_loc, symbol in sym_dict.items():
        if symbol != '*':
            continue
        nums = []
        for n_loc, num in num_dict.items():
            if compare(n_loc, s_loc):
                nums.append(num)
        if len(nums) != 2:
            continue
        temp = 1
        for n in nums:
            temp *= n
        total += temp
    return total


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 550934
# Part 2 solution: 81997870
