from re import findall


def read_data():
    file = 'Days/Day06/input.txt'
    with open(file, 'r') as f:
        lines = f.read().split('\n')[:-1]
    data = []
    for line in lines:
        data.append([int(num) for num in findall(r'\d+', line)])
    return data


def p1(data: list[list[int]]) -> int:
    times, distances = data
    wins = []

    for i in range(len(times)):
        time_limit = times[i]
        distance_record = distances[i]
        win_count = 0

        for hold_time in range(1, time_limit-1):
            distance_travel = hold_time * (time_limit-hold_time)
            if distance_travel > distance_record:
                win_count += 1
        wins.append(win_count)

    total = 1
    for w in wins:
        total *= w
    return total


def p2(data: list[list[int]]) -> int:
    time_limit = int(''.join([str(num) for num in data[0]]))
    distance_record = int(''.join([str(num) for num in data[1]]))
    win_count = 0

    for hold_time in range(1, time_limit-1):
        distance_travel = hold_time * (time_limit-hold_time)
        if distance_travel > distance_record:
            win_count += 1
    return win_count


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 771628
# Part 2 solution: 27363861
