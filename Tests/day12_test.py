from Days.Day12.day_12 import p1, p2, parse


def test_p1():
    test_data = [
        '???.### 1,1,3',
        '.??..??...?##. 1,1,3',
        '?#?#?#?#?#?#?#? 1,3,1,6',
        '????.#...#... 4,1,1',
        '????.######..#####. 1,6,5',
        '?###???????? 3,2,1'
    ]
    assert p1(parse(test_data)) == 21


def test_p2():
    test_data = [

    ]
    assert p2(parse(test_data)) == -1
