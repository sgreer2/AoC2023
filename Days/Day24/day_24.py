from __future__ import annotations
from re import findall


def read_data():
    file = 'Days/Day24/input.txt'
    with open(file, 'r') as f:
        return [Hailstone(line) for line in f.read().split('\n')[:-1]]


class Hailstone:
    x: int
    y: int
    z: int

    vx: int
    vy: int
    vz: int

    def __init__(self, data: str) -> None:
        nums = [int(num) for num in findall(r'-?\d+', data)]
        self.x, self.y, self.z, self.vx, self.vy, self.vz = nums

    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z}) : ({self.vx}, {self.vy}, {self.vz})'

    def _get_second_point(self, min_range: int, max_range: int) -> tuple[int, int, int]:
        vx_positive = True if self.vx > 0 else False
        vy_positive = True if self.vy > 0 else False

        x_dist = 0
        if vx_positive:
            x_dist = max_range - self.x
        else:
            x_dist = min_range - self.x

        y_dist = 0
        if vy_positive:
            y_dist = max_range - self.y
        else:
            y_dist = min_range - self.y

        x_time = x_dist / self.vx
        y_time = y_dist / self.vy

        time = max(x_time, y_time)

        x2 = round(self.x + (self.vx * time))
        y2 = round(self.y + (self.vy * time))

        return (x2, y2, self.z)

    def intersect_xy(self, other: Hailstone, min_range: int, max_range: int):
        '''Return True if the 2 vertices intersect (x&y vertices only) within the given ranges'''

        second_point = self._get_second_point(min_range, max_range)
        a1 = second_point[1] - self.y
        b1 = self.x - second_point[0]
        c1 = (a1*self.x) + (b1*self.y)

        other_second_point = other._get_second_point(min_range, max_range)
        a2 = other_second_point[1] - other.y
        b2 = other.x - other_second_point[0]
        c2 = (a2*other.x) + (b2*other.y)

        determinant = (a1*b2) - (a2*b1)

        if determinant == 0:  # Lines are parallel
            return False
        x = ((b2*c1) - (b1*c2)) / determinant
        y = ((a1*c2) - (a2*c1)) / determinant

        # checking if intersection happened in the past
        if self.x < x and self.vx < 0:
            return False
        if self.x > x and self.vx > 0:
            return False
        if self.y < y and self.vy < 0:
            return False
        if self.y > y and self.vy > 0:
            return False

        if other.x < x and other.vx < 0:
            return False
        if other.x > x and other.vx > 0:
            return False
        if other.y < y and other.vy < 0:
            return False
        if other.y > y and other.vy > 0:
            return False

        if x < min_range or x > max_range:
            return False
        if y < min_range or y > max_range:
            return False

        return True


def p1(hailstones: list[Hailstone],
       min_range: int = 200_000_000_000_000,
       max_range: int = 400_000_000_000_000
       ) -> int:
    intersects = 0
    for index in range(len(hailstones)-1):
        stone = hailstones[index]
        for index_2 in range(index+1, len(hailstones)):
            stone_2 = hailstones[index_2]
            if stone.intersect_xy(stone_2, min_range, max_range):
                intersects += 1
    return intersects


def p2(data) -> int:
    return -1


def main():
    hailstones = read_data()
    s1, s2 = p1(hailstones), p2(hailstones)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 14046
# Part 2 solution:
