from collections import deque


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


def p1(pipe_map: list[str]) -> int:
    best_distances = {}

    start = (0, 0)
    for y, line in enumerate(pipe_map):
        index = line.find('S')
        if index != -1:
            start = (index, y)
            break

    neighbours = PIPES['S']
    best_distances[start] = 0
    queue = deque()
    for x, y in neighbours:
        s_x, s_y = start
        steps = best_distances[start]
        n_x, n_y = s_x+x, s_y+y
        n_char = pipe_map[n_y][n_x]
        n_pos = (n_x, n_y)
        if is_connected(start, n_pos, n_char):
            queue.append(n_pos)
            best_distances[n_pos] = steps+1

    while len(queue) > 0:
        current_pos = queue.popleft()
        steps = best_distances[current_pos]
        current_x, current_y = current_pos
        current_char = pipe_map[current_y][current_x]
        neighbours = PIPES[current_char]
        for x, y in neighbours:
            n_x, n_y = current_x+x, current_y+y
            n_pos = (n_x, n_y)
            if n_pos not in best_distances.keys():
                queue.append(n_pos)
                best_distances[n_pos] = steps+1
                continue
            if steps+1 < best_distances[n_pos]:
                queue.append(n_pos)
                best_distances[n_pos] = steps+1

    furthest = 0
    for distance in best_distances.values():
        furthest = max(distance, furthest)
    return furthest


def p2(pipe_map: list[str]) -> int:
    return -1


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 6733
# Part 2 solution:
