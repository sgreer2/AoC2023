from enum import Enum


def read_data():
    file = 'Days/Day23/input.txt'
    with open(file, 'r') as f:
        return f.read().split('\n')[:-1]


class D(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)


def _get_directions(last_dir: D) -> list[D]:
    if last_dir == D.NORTH:
        return [D.NORTH, D.EAST, D.WEST]
    if last_dir == D.EAST:
        return [D.NORTH, D.EAST, D.SOUTH]
    if last_dir == D.SOUTH:
        return [D.EAST, D.SOUTH, D.WEST]
    return [D.NORTH, D.SOUTH, D.WEST]


def _check_slope(char: str, direction: D) -> bool:
    if direction == D.NORTH and char == '^':
        return True
    if direction == D.EAST and char == '>':
        return True
    if direction == D.SOUTH and char == 'v':
        return True
    if direction == D.WEST and char == '<':
        return True
    return False


def _solve(hiking_map: list[str], hike_lengths: list[int], cur_pos: tuple[int, int], last_dir: D, steps: int, goal: tuple[int, int]):

    while True:
        if cur_pos == goal:
            hike_lengths.append(steps)
            return
        directions = _get_directions(last_dir)
        step_options: list[tuple[tuple[int, int], D]] = []
        for d in directions:
            n_pos_x, n_pos_y = cur_pos[0]+d.value[0], cur_pos[1]+d.value[1]
            hike_char = hiking_map[n_pos_y][n_pos_x]
            if hike_char == '#':
                continue
            if hike_char == '.':
                step_options.append(((n_pos_x, n_pos_y), d))
                continue
            if _check_slope(hike_char, d):
                step_options.append(((n_pos_x, n_pos_y), d))

        if len(step_options) == 1:
            steps += 1
            cur_pos = step_options[0][0]
            last_dir = step_options[0][1]
            continue

        for pos, d in step_options:
            _solve(hiking_map, hike_lengths, pos, d, steps+1, goal)
        break


def p1(hiking_map: list[str]) -> int:
    start = (1, 0)
    end = (len(hiking_map[0])-2, len(hiking_map)-1)
    hike_lengths = []

    _solve(hiking_map, hike_lengths, start, D.SOUTH, 0, end)

    return max(hike_lengths)


def p2(hiking_map: list[str]) -> int:
    return -1


def main():
    hiking_map = read_data()
    s1, s2 = p1(hiking_map), p2(hiking_map)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 2202
# Part 2 solution:
