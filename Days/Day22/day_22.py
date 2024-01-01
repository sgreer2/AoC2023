from __future__ import annotations
from re import findall
from copy import deepcopy


def read_data():
    file = 'Days/Day22/input.txt'
    with open(file, 'r') as f:
        return [Brick(line, str(i)) for i, line in enumerate(f.read().split('\n')[:-1])]


class Brick:
    # x,y,z format (z is vertical)
    id: str
    start: tuple[int, int, int]
    end: tuple[int, int, int]
    lowest_point: int
    highest_point: int

    def __init__(self, data: str, id: str = '') -> None:
        self.id = id
        nums = [int(num) for num in findall(r'\d+', data)]
        self.start = (nums[0], nums[1], nums[2])
        self.end = (nums[3], nums[4], nums[5])
        self.lowest_point = nums[2]
        self.highest_point = nums[5]

    def __lt__(self, other: Brick) -> bool:
        if self.lowest_point == other.lowest_point:
            if self.highest_point == other.highest_point:
                return True
            return self.highest_point < other.highest_point
        return self.lowest_point < other.lowest_point

    def brick_overlap_horizontal(self, other: Brick) -> bool:
        x_range = (self.start[0], self.end[0])
        y_range = (self.start[1], self.end[1])

        other_x_range = (other.start[0], other.end[0])
        other_y_range = (other.start[1], other.end[1])

        # Check X range
        x_in_range = False
        if other_x_range[0] >= x_range[0] and other_x_range[0] <= x_range[1]:
            x_in_range = True
        elif other_x_range[1] >= x_range[0] and other_x_range[1] <= x_range[1]:
            x_in_range = True
        elif x_range[0] >= other_x_range[0] and x_range[0] <= other_x_range[1]:
            x_in_range = True
        elif x_range[1] >= other_x_range[0] and x_range[1] <= other_x_range[1]:
            x_in_range = True

        if not x_in_range:
            return False

        # Check Y range (only if X is within range)
        y_in_range = False
        if other_y_range[0] >= y_range[0] and other_y_range[0] <= y_range[1]:
            y_in_range = True
        elif other_y_range[1] >= y_range[0] and other_y_range[1] <= y_range[1]:
            y_in_range = True
        elif y_range[0] >= other_y_range[0] and y_range[0] <= other_y_range[1]:
            y_in_range = True
        elif y_range[1] >= other_y_range[0] and y_range[1] <= other_y_range[1]:
            y_in_range = True

        if y_in_range:
            return True
        return False

    def move(self, new_z: int) -> None:
        z_diff = self.end[2] - self.start[2]
        x, y, _ = self.start
        self.start = (x, y, new_z)
        x2, y2, _ = self.end
        self.end = (x2, y2, new_z + z_diff)
        self.lowest_point = new_z
        self.highest_point = new_z + z_diff

    def get_points(self) -> list[tuple[int, int, int]]:
        points = []
        for x in range(self.start[0], self.end[0]+1):
            for y in range(self.start[1], self.end[1]+1):
                for z in range(self.start[2], self.end[2]+1):
                    points.append((x, y, z))
        return points

    def __str__(self) -> str:
        return f'{self.id} -> {self.start}:{self.end} --- ^{self.highest_point}^  v{self.lowest_point}v'


def _drop_sand_bricks(bricks: list[Brick]) -> list[Brick]:
    bricks = deepcopy(bricks)
    bricks.sort()
    moved_bricks: list[Brick] = []
    for brick in bricks:
        if brick.lowest_point == 1:
            moved_bricks.append(brick)
            continue
        new_z = 0
        for other_brick in moved_bricks:
            if other_brick.brick_overlap_horizontal(brick):
                new_z = max(new_z, other_brick.highest_point)

        new_z += 1
        brick.move(new_z)
        moved_bricks.append(brick)
    moved_bricks.sort()
    return moved_bricks


def p1(bricks: list[Brick]) -> int:
    bricks = _drop_sand_bricks(bricks)

    dissintegrate_count = 0
    for brick in bricks:
        above_bricks: list[Brick] = []
        for a_brick in bricks:
            # Check if it's at the correct Z level
            if a_brick.lowest_point == brick.highest_point+1:
                # Check if the X & Y Axis overlap
                if brick.brick_overlap_horizontal(a_brick):
                    above_bricks.append(a_brick)
        if len(above_bricks) == 0:
            dissintegrate_count += 1
            continue
        can_disintegrate = True
        for a_brick in above_bricks:
            below_bricks: list[Brick] = []
            for b_brick in bricks:
                # Check if it's at the correct Z level
                if a_brick.lowest_point == b_brick.highest_point+1:
                    # Check if the X & Y Axis overlap
                    if a_brick.brick_overlap_horizontal(b_brick):
                        below_bricks.append(b_brick)
            if len(below_bricks) == 1:
                can_disintegrate = False
                break
        if can_disintegrate:
            dissintegrate_count += 1

    return dissintegrate_count


def p2(bricks: list[Brick]) -> int:
    return -1


def main():
    bricks = read_data()
    s1, s2 = p1(bricks), p2(bricks)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 391
# Part 2 solution:
