from Days.Day03.day_03 import p1, p2, parse


def test_p1():
    test_data = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..'
    ]
    assert p1(parse(test_data)) == 4361


def test_p2():
    test_data = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..'
    ]
    assert p2(parse(test_data)) == 467835
