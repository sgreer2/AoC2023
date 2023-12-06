from Days.Day06.day_06 import p1, p2


def test_p1():
    test_data = [
        [7, 15, 30],
        [9, 40, 200]
    ]
    assert p1(test_data) == 288


def test_p2():
    test_data = [
        [7, 15, 30],
        [9, 40, 200]
    ]
    assert p2(test_data) == 71503
