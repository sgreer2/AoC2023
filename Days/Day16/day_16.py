from enum import IntEnum


class Direction(IntEnum):
    North = 1
    East = 2
    South = 3
    West = 4


class Beam:
    x: int
    y: int
    direction: Direction

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.direction = Direction.East

    def _get_pos(self) -> tuple[int, int]:
        return (self.x, self.y)

    def move(self, x: int = 0, y: int = 0):
        if x != 0 or y != 0:
            self.x += x
            self.y += y
            return
        if self.direction == Direction.North:
            self.y -= 1
            return
        if self.direction == Direction.South:
            self.y += 1
            return
        if self.direction == Direction.West:
            self.x -= 1
            return
        if self.direction == Direction.East:
            self.x += 1
            return

    def split(self):
        return Beam(self.x, self.y)


def read_data():
    file = 'Days/Day16/input.txt'
    with open(file, 'r') as f:
        return f.read().split('\n')[:-1]


def p1(contraption_map: list[str]) -> int:
    visited: list[tuple[tuple[int, int], Direction]] = []
    beams: list[Beam] = []
    beams.append(Beam(0, 0))
    for beam in beams:
        while True:
            cur_x, cur_y = beam._get_pos()

            # check if in range
            if cur_x < 0 or cur_y < 0:
                break
            if cur_x >= len(contraption_map[0]) or cur_y >= len(contraption_map[1]):
                break
            if ((cur_x, cur_y), beam.direction) in visited:
                break

            # add to visited
            visited.append(((cur_x, cur_y), beam.direction))

            # figure out next position
            pos_char = contraption_map[cur_y][cur_x]
            if pos_char == '.':
                beam.move()
                continue
            if pos_char == '|':
                if beam.direction in [Direction.North, Direction.South]:
                    beam.move()
                    continue
                new_beam = beam.split()
                new_beam.move(y=1)
                new_beam.direction = Direction.South
                beams.append(new_beam)

                beam.move(y=-1)
                beam.direction = Direction.North

            if pos_char == '-':
                if beam.direction in [Direction.East, Direction.West]:
                    beam.move()
                    continue
                new_beam = beam.split()
                new_beam.move(x=1)
                new_beam.direction = Direction.East
                beams.append(new_beam)

                beam.move(x=-1)
                beam.direction = Direction.West

            if pos_char == '/':
                x, y = 0, 0
                new_dir = Direction.North
                if beam.direction == Direction.North:
                    new_dir = Direction.East
                    x = 1
                elif beam.direction == Direction.South:
                    new_dir = Direction.West
                    x = -1
                elif beam.direction == Direction.East:
                    new_dir = Direction.North
                    y = -1
                elif beam.direction == Direction.West:
                    new_dir = Direction.South
                    y = 1
                beam.move(x=x, y=y)
                beam.direction = new_dir

            if pos_char == '\\':
                x, y = 0, 0
                new_dir = Direction.North
                if beam.direction == Direction.North:
                    new_dir = Direction.West
                    x = -1
                elif beam.direction == Direction.South:
                    new_dir = Direction.East
                    x = 1
                elif beam.direction == Direction.East:
                    new_dir = Direction.South
                    y = 1
                elif beam.direction == Direction.West:
                    new_dir = Direction.North
                    y = -1
                beam.move(x=x, y=y)
                beam.direction = new_dir

    temp = []
    for pos, _ in visited:
        if pos in temp:
            continue
        temp.append(pos)
    return len(temp)


def p2(data) -> int:
    return -1


def main():
    contraption_map = read_data()
    s1, s2 = p1(contraption_map), p2(contraption_map)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 8034
# Part 2 solution:
