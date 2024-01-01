from Days.Day22.day_22 import p1, p2, Brick


def test_p1():
    test_data = [
        '1,0,1~1,2,1',
        '0,0,2~2,0,2',
        '0,2,3~2,2,3',
        '0,0,4~0,2,4',
        '2,0,5~2,2,5',
        '0,1,6~2,1,6',
        '1,1,8~1,1,9'
    ]
    bricks = [Brick(line) for line in test_data]
    assert p1(bricks) == 5


# def test_p2():
#     test_data = [
#         '1,0,1~1,2,1',
#         '0,0,2~2,0,2',
#         '0,2,3~2,2,3',
#         '0,0,4~0,2,4',
#         '2,0,5~2,2,5',
#         '0,1,6~2,1,6',
#         '1,1,8~1,1,9'
#     ]
#     bricks = [Brick(line) for line in test_data]
#     assert p2(bricks) == 7
