from Days.Day07.day_07 import p1, p2


def test_p1():
    test_data = [
        ('32T3K', 765),
        ('T55J5', 684),
        ('KK677', 28),
        ('KTJJT', 220),
        ('QQQJA', 483)
    ]
    assert p1(test_data) == 6440


def test_p2():
    test_data = [
        ('32T3K', 765),
        ('T55J5', 684),
        ('KK677', 28),
        ('KTJJT', 220),
        ('QQQJA', 483)
    ]
    assert p2(test_data) == 5905
