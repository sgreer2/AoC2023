from functools import cache


def read_data():
    file = 'Days/Day12/input.txt'
    with open(file, 'r') as f:
        return parse(f.read().split('\n')[:-1])


def parse(array: list[str]) -> list[tuple[str, tuple[int]]]:
    new_array = []
    for line in array:
        string, nums = line.split()
        new_array.append(
            (string, tuple([int(num) for num in nums.split(',')]))
        )

    return new_array


def _unfold(spots: str, nums: tuple[int, ...]) -> tuple[str, tuple[int, ...]]:
    new_string = '?'.join([spots] * 5)
    return (new_string, nums*5)


@cache
def _solve(spots: str, nums: tuple[int, ...]) -> int:
    total = 0

    cur_num = nums[0]
    next_nums = ()

    if len(nums) > 1:
        next_nums = tuple(nums[1:])

    for index, char in enumerate(spots):
        if char == '.':
            continue
        if cur_num + index > len(spots):
            break
        place = spots[index:index+cur_num]
        if '.' in place:
            continue
        if '#' in spots[:index]:
            break
        if index+cur_num != len(spots) and spots[index+cur_num] == '#':
            continue

        if len(next_nums) > 0:
            total += _solve(spots[index+cur_num+1:], next_nums)
        else:
            if '#' in spots[index+cur_num+1:]:
                continue
            total += 1

        if char == '#':
            break

    return total


def p1(spring_data: list[tuple[str, tuple[int, ...]]]) -> int:
    total_arrangements = 0
    for spots, nums in spring_data:
        total_arrangements += _solve(spots, nums)
    return total_arrangements


def p2(spring_data: list[tuple[str, tuple[int, ...]]]) -> int:
    total_arrangements = 0
    for spots, nums in spring_data:
        unfolded_spots, unfolded_nums = _unfold(spots, nums)
        total_arrangements += _solve(unfolded_spots, unfolded_nums)
    return total_arrangements


def main():
    spring_data = read_data()
    s1, s2 = p1(spring_data), p2(spring_data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 7653
# Part 2 solution: 60681419004564
