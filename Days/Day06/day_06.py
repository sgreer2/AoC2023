from re import findall


def read_data():
    file = 'Days/Day06/input.txt'
    with open(file, 'r') as f:
        lines = f.read().split('\n')[:-1]
    data = []
    for line in lines:
        data.append([int(num) for num in findall(r'\d+', line)])
    return data


def _wins(hold_time: int, time_limit: int, record: int) -> bool:
    if record < hold_time * (time_limit-hold_time):
        return True
    return False


def p1(data: list[list[int]]) -> int:
    times, distances = data
    total = 1
    for i in range(len(times)):
        time_limit = times[i]
        distance_record = distances[i]
        left_num = 0
        right_num = 0
        for i in range(1, time_limit):
            if _wins(i, time_limit, distance_record):
                left_num = i
                break
        for i in range(time_limit-1, 0, -1):
            if _wins(i, time_limit, distance_record):
                right_num = i
                break
        total *= (right_num-left_num)+1

    return total


def p2(data: list[list[int]]) -> int:
    time_limit = int(''.join([str(num) for num in data[0]]))
    distance_record = int(''.join([str(num) for num in data[1]]))
    left_num = 0
    right_num = 0
    for i in range(1, time_limit):
        if _wins(i, time_limit, distance_record):
            left_num = i
            break
    for i in range(time_limit, 0, -1):
        if _wins(i, time_limit, distance_record):
            right_num = i
            break
    return (right_num - left_num)+1


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 771628
# Part 2 solution: 27363861
