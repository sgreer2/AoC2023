from Days.Day09.day_09 import p1, p2


def test_p1():
    test_data = [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45]
    ]
    assert p1(test_data) == 114


def test_p2():
    test_data = [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45]
    ]
    assert p2(test_data) == 2
