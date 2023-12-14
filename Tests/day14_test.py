from Days.Day14.day_14 import p1, p2


def test_p1():
    test_data = [
        'O....#....',
        'O.OO#....#',
        '.....##...',
        'OO.#O....O',
        '.O.....O#.',
        'O.#..O.#.#',
        '..O..#O..O',
        '.......O..',
        '#....###..',
        '#OO..#....'
    ]
    assert p1(test_data) == 136


# def test_p2():
#     test_data = [

#     ]
#     assert p2(test_data) == -1
