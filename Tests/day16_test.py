from Days.Day16.day_16 import p1, p2


def test_p1():
    test_data = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''
    assert p1(str(test_data).split('\n')) == 46


def test_p2():
    test_data = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''
    assert p2(str(test_data).split('\n')) == 51
