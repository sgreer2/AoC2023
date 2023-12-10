from Days.Day10.day_10 import p1, p2


def test_p1():
    test_data = [
        '.....',
        '.S-7.',
        '.|.|.',
        '.L-J.',
        '.....'
    ]
    assert p1(test_data) == 4


def test_p1_v2():
    test_data = [
        '..F7.',
        '.FJ|.',
        'SJ.L7',
        '|F--J',
        'LJ...'
    ]
    assert p1(test_data) == 8


def test_p2():
    test_data = [
        '...........',
        '.S-------7.',
        '.|F-----7|.',
        '.||.....||.',
        '.||.....||.',
        '.|L-7.F-J|.',
        '.|..|.|..|.',
        '.L--J.L--J.',
        '...........'
    ]
    assert p2(test_data) == 4


def test_p2_v2():
    test_data = [
        '.F----7F7F7F7F-7....',
        '.|F--7||||||||FJ....',
        '.||.FJ||||||||L7....',
        'FJL7L7LJLJ||LJ.L-7..',
        'L--J.L7...LJS7F-7L7.',
        '....F-J..F7FJ|L7L7L7',
        '....L7.F7||L7|.L7L7|',
        '.....|FJLJ|FJ|F7|.LJ',
        '....FJL-7.||.||||...',
        '....L---J.LJ.LJLJ...'
    ]
    assert p2(test_data) == 8


def test_p2_v3():
    test_data = [
        'FF7FSF7F7F7F7F7F---7',
        'L|LJ||||||||||||F--J',
        'FL-7LJLJ||||||LJL-77',
        'F--JF--7||LJLJ7F7FJ-',
        'L---JF-JLJ.||-FJLJJ7',
        '|F|F-JF---7F7-L7L|7|',
        '|FFJF7L7F-JF7|JL---7',
        '7-L-JL7||F7|L7F-7F7|',
        'L.L7LFJ|||||FJL7||LJ',
        'L7JLJL-JLJLJL--JLJ.L'
    ]
    assert p2(test_data) == 10
