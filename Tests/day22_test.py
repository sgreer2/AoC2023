from Days.Day22.day_22 import p1, p2, data_to_dict


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
    assert p1(data_to_dict(test_data)) == 5


def test_p2():
    test_data = [
        '1,0,1~1,2,1',
        '0,0,2~2,0,2',
        '0,2,3~2,2,3',
        '0,0,4~0,2,4',
        '2,0,5~2,2,5',
        '0,1,6~2,1,6',
        '1,1,8~1,1,9'
    ]
    assert p2(data_to_dict(test_data)) == 7
