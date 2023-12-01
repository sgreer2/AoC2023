from Days.Day01.day_01 import p1, p2


def test_p1():
    test_data = [
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet'
    ]
    assert p1(test_data) == 142


def test_p2():
    test_data = [
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen'
    ]
    assert p2(test_data) == 281
