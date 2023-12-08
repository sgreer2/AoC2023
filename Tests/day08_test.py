from Days.Day08.day_08 import p1, p2


def test_p1():
    inst = [0, 0, 1]
    nodes = {
        'AAA': ('BBB', 'BBB'),
        'BBB': ('AAA', 'ZZZ'),
        'ZZZ': ('ZZZ', 'ZZZ')
    }
    assert p1(inst, nodes) == 6


def test_p2():
    inst = [0, 1]
    nodes = {
        '11A': ('11B', 'XXX'),
        '11B': ('XXX', '11Z'),
        '11Z': ('11B', 'XXX'),
        '22A': ('22B', 'XXX'),
        '22B': ('22C', '22C'),
        '22C': ('22Z', '22Z'),
        '22Z': ('22B', '22B'),
        'XXX': ('XXX', 'XXX')
    }
    assert p2(inst, nodes) == 6
