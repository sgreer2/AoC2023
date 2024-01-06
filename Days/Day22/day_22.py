from __future__ import annotations
from collections import deque
from re import findall


def read_data():
    file = 'Days/Day22/input.txt'
    with open(file, 'r') as f:
        return data_to_dict(f.read().split('\n')[:-1])


def data_to_dict(lines: list[str]) -> dict:
    sand_bricks = dict()
    for line in lines:
        nums = [int(num) for num in findall(r'\d+', line)]
        pos: tuple = (tuple(nums[:3]), tuple(nums[3:]))
        min_height = nums[2]
        sand_bricks[pos] = min_height
    return _get_dropped_sand(dict(sorted(sand_bricks.items(), key=lambda x: x[1])))


def _get_dropped_sand(bricks: dict[tuple[tuple[int, int, int], tuple[int, int, int]], int]) -> dict:
    dropped_sand_bricks: dict[tuple[tuple[int, int, int], tuple[int, int, int]],
                              tuple[list[tuple], list[tuple]]] = dict()
    for pos in bricks.keys():
        highest = 0
        found_bricks = []
        for other_pos in dropped_sand_bricks.keys():
            if _overlap(pos, other_pos):
                other_highest = other_pos[1][2]
                if other_highest < highest:
                    continue
                if other_highest == highest:
                    found_bricks.append(other_pos)
                    continue
                highest = other_highest
                found_bricks = [other_pos]

        new_z = highest+1
        x, y, z = pos[0]
        x2, y2, z2 = pos[1]
        offset = z2 - z
        new_pos_a: tuple = (x, y, new_z)
        new_pos_b: tuple = (x2, y2, new_z + offset)
        new_pos: tuple = (new_pos_a, new_pos_b)

        dropped_sand_bricks[new_pos] = ([], [])

        for brick in found_bricks:
            dropped_sand_bricks[new_pos][0].append(brick)
            dropped_sand_bricks[brick][1].append(new_pos)

    return dropped_sand_bricks


def _overlap(primary: tuple[tuple[int, int, int], tuple[int, int, int]], secondary: tuple[tuple[int, int, int], tuple[int, int, int]]) -> bool:
    p_a, p_b = primary
    s_a, s_b = secondary

    p_min_x, p_min_y, _ = p_a
    p_max_x, p_max_y, _ = p_b

    s_min_x, s_min_y, _ = s_a
    s_max_x, s_max_y, _ = s_b

    x_in_range = False
    if p_min_x <= s_min_x <= p_max_x or p_min_x <= s_max_x <= p_max_x:
        x_in_range = True
    elif s_min_x <= p_min_x <= s_max_x or s_min_x <= p_max_x <= s_max_x:
        x_in_range = True

    if not x_in_range:
        return False

    y_in_range = False
    if p_min_y <= s_min_y <= p_max_y or p_min_y <= s_max_y <= p_max_y:
        y_in_range = True
    if s_min_y <= p_min_y <= s_max_y or s_min_y <= p_max_y <= s_max_y:
        y_in_range = True

    if not y_in_range:
        return False
    return True


def p1(sand_bricks: dict) -> int:
    count = 0
    for _, above in sand_bricks.values():
        if len(above) == 0:
            count += 1
            continue
        for a_pos in above:
            a_below, _ = sand_bricks[a_pos]
            if len(a_below) == 1:
                break
        else:
            # Executes only if the for loop doesn't encounter a break
            count += 1
    return count


def p2(sand_bricks: dict) -> int:
    total = 0

    sorted_sand_bricks = dict(
        sorted(
            sand_bricks.items(),
            key=lambda x: x[0][1][2],
            reverse=True
        )
    )

    for pos in sorted_sand_bricks.keys():
        can_fall = set()
        queue = deque()
        queue.append(pos)

        while queue:
            c_brick = queue.popleft()
            _, above_bricks = sorted_sand_bricks[c_brick]
            if len(above_bricks) == 0:
                continue

            for a_brick in above_bricks:
                below_bricks, _ = sorted_sand_bricks[a_brick]
                if len(below_bricks) == 1:
                    queue.append(a_brick)
                    can_fall.add(a_brick)
                    continue
                valid = True
                for b_brick in below_bricks:
                    if b_brick == c_brick:
                        continue
                    if b_brick not in can_fall:
                        valid = False
                        break
                if valid:
                    queue.append(a_brick)
                    can_fall.add(a_brick)

        total += len(can_fall)

    return total


def main():
    sand_bricks = read_data()
    s1, s2 = p1(sand_bricks), p2(sand_bricks)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 391
# Part 2 solution: 69601
