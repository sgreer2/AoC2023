from Days.Day24.day_24 import p1, p2, Hailstone


def test_p1():
    test_data = [
        '19, 13, 30 @ -2,  1, -2',
        '18, 19, 22 @ -1, -1, -2',
        '20, 25, 34 @ -2, -2, -4',
        '12, 31, 28 @ -1, -2, -1',
        '20, 19, 15 @  1, -5, -3'
    ]
    assert p1([Hailstone(line) for line in test_data], 7, 27) == 2


# def test_p2():
#     test_data = [

#     ]
#     assert p2(test_data) == -1
