from Days.Day15.day_15 import p1, p2, string_to_hash


def test_hash():
    test_data = 'HASH'
    assert string_to_hash(test_data) == 52


def test_p1():
    test_data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
    assert p1(test_data) == 1320


def test_p2():
    test_data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
    assert p2(test_data) == 145
