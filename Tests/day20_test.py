from Days.Day20.day_20 import p1, p2, _module_parse


def test_p1_v1():
    test_data = [
        'broadcaster -> a, b, c',
        '%a -> b',
        '%b -> c',
        '%c -> inv',
        '&inv -> a'
    ]
    assert p1(_module_parse(test_data)) == 32000000


def test_p1_v2():
    test_data = [
        'broadcaster -> a',
        '%a -> inv, con',
        '&inv -> b',
        '%b -> con',
        '&con -> output'
    ]
    assert p1(_module_parse(test_data)) == 11687500

# def test_p2():
#     test_data = [

#     ]
#     assert p2(test_data) == -1
