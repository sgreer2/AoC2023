
def read_data():
    file = 'Days/Day11/input.txt'
    with open(file, 'r') as f:
        raw_data = f.read().split('\n')[:-1]
    star_map = convert_star_map(raw_data)
    return star_map


def convert_star_map(array: list[str]) -> list[list[int]]:
    new_array = []
    for line in array:
        line = line.replace('.', '0')
        line = line.replace('#', '1')
        new_array.append([int(num) for num in list(line)])
    return new_array


def _get_column(array, col):
    return [row[col] for row in array]


def _solve(star_map: list[list[int]], age: int = 1) -> int:
    if age != 1:
        age -= 1
    galaxys = []
    empty_rows = []
    empty_cols = []

    for y in range(len(star_map)):
        if any(star_map[y]):
            for x in range(len(star_map[y])):
                if star_map[y][x] == 1:
                    galaxys.append((x, y))
            continue
        empty_rows.append(y)
    for x in range(len(star_map[0])):
        col = _get_column(star_map, x)
        if any(col):
            continue
        empty_cols.append(x)

    distances = []
    for index, pos in enumerate(galaxys[:-1]):
        x, y = pos
        for b_pos in galaxys[index+1:]:
            b_x, b_y = b_pos
            extra_count = 0
            x_min, x_max = min(x, b_x), max(x, b_x)
            y_min, y_max = min(y, b_y), max(y, b_y)
            for r in empty_rows:
                if y_min < r < y_max:
                    extra_count += age
            for r in empty_cols:
                if x_min < r < x_max:
                    extra_count += age
            distance = (x_max - x_min) + (y_max - y_min)
            distances.append(distance + extra_count)
    return sum(distances)


def p1(star_map: list[list[int]]) -> int:
    return _solve(star_map)


def p2(star_map: list[list[int]], age: int = 1_000_000) -> int:
    return _solve(star_map, age)


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 9177603
# Part 2 solution: 632003913611
