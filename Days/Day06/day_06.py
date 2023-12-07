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
    total = 1
    for i in range(len(times)):
        time_limit = times[i]
        distance_record = distances[i]
        left_index = 0
        for i in range(1, time_limit):
            if distance_record < i * (time_limit-i):
                left_index = i
                break
        total *= (time_limit-(left_index * 2))+1

    return total


def p2(data: list[list[int]]) -> int:
    time_limit = int(''.join([str(num) for num in data[0]]))
    distance_record = int(''.join([str(num) for num in data[1]]))
    left_index = 0
    for i in range(1, time_limit):
        if distance_record < i * (time_limit-i):
            left_index = i
            break
    return (time_limit-(left_index * 2))+1


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 771628
# Part 2 solution: 27363861
