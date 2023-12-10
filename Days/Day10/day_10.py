from math import floor
from matplotlib.path import Path


def read_data():
    file = 'Days/Day10/input.txt'
    with open(file, 'r') as f:
        return f.read().split('\n')


PIPES = {
    '|': ((0, -1), (0, 1)),
    '-': ((-1, 0), (1, 0)),
    'L': ((0, -1), (1, 0)),
    'J': ((0, -1), (-1, 0)),
    '7': ((-1, 0), (0, 1)),
    'F': ((1, 0), (0, 1)),
    '.': (),
    'S': ((0, -1), (0, 1), (-1, 0), (1, 0))
}


def is_connected(current: tuple[int, int], next: tuple[int, int], next_char: str) -> bool:
    neighbours = PIPES[next_char]
    for x, y in neighbours:
        if current == (next[0]+x, next[1]+y):
            return True
    return False


def get_track_map(pipe_map: list[str]) -> list[tuple[int, int]]:
    track = []
    start = (0, 0)
    for y, line in enumerate(pipe_map):
        index = line.find('S')
        if index != -1:
            start = (index, y)
            break

    neighbours = PIPES['S']
    track.append(start)
    current_pos = start
    previous_pos = start

    for x, y in neighbours:
        s_x, s_y = current_pos
        n_x, n_y = s_x+x, s_y+y
        n_char = pipe_map[n_y][n_x]
        n_pos = (n_x, n_y)
        if is_connected(start, n_pos, n_char):
            previous_pos = current_pos
            current_pos = n_pos
            break

    while current_pos != start:
        track.append(current_pos)
        current_x, current_y = current_pos
        current_char = pipe_map[current_y][current_x]
        neighbours = PIPES[current_char]
        for x, y in neighbours:
            n_x, n_y = current_x+x, current_y+y
            n_pos = (n_x, n_y)
            if n_pos == previous_pos:
                continue
            previous_pos = current_pos
            current_pos = n_pos
            break
    return track


def p1(pipe_map: list[str]) -> int:
    track = get_track_map(pipe_map)
    return floor(len(track)/2)


def p2(pipe_map: list[str]) -> int:
    enclosed_count = 0
    track = get_track_map(pipe_map)
    track_path = Path(track)
    for y in range(len(pipe_map)):
        for x in range(len(pipe_map[y])):
            pos = (x, y)
            if pos in track:
                continue
            if track_path.contains_point(pos):
                enclosed_count += 1
    return enclosed_count


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 6733
# Part 2 solution: 435
