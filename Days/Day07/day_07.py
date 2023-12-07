from enum import IntEnum
from collections import deque


def read_data() -> list[tuple[str, int]]:
    file = 'Days/Day07/input.txt'
    with open(file, 'r') as f:
        lines = f.read().split('\n')[:-1]
    return [(hand, int(bid)) for hand, bid in [line.split(' ') for line in lines]]


class Hand_Types(IntEnum):
    Five = 7
    Four = 6
    Full = 5
    Three = 4
    Two_Pair = 3
    One_Pair = 2
    High = 1


def _solve_hand_type(cards: str, part2: bool = False) -> Hand_Types:
    uniques = set(cards)
    counts = {}
    for c in uniques:
        counts[c] = cards.count(c)
    if part2:
        highest_char, highest_count = 'A', 0

        for key, val in counts.items():
            if key == 'J':
                continue
            if highest_count < val:
                highest_count = val
                highest_char = key

        cards = cards.replace('J', highest_char)

    uniques = set(cards)
    counts = {}
    for c in uniques:
        counts[c] = cards.count(c)
    if len(uniques) == 1:
        return Hand_Types.Five
    if len(uniques) == 4:
        return Hand_Types.One_Pair
    if len(uniques) == 5:
        return Hand_Types.High

    if len(uniques) == 2 and 4 in counts.values():
        return Hand_Types.Four

    if len(uniques) == 2 and 3 in counts.values():
        return Hand_Types.Full

    if 3 in counts.values() and len(uniques) > 2:
        return Hand_Types.Three

    # Two_pair
    return Hand_Types.Two_Pair


def p1(hands: list[tuple[str, int]]) -> int:
    CARDS = 'AKQJT98765432'
    solved_hands: deque[tuple[Hand_Types, str, int]] = deque()
    for hand in hands:
        cards, bid = hand
        hand_type = _solve_hand_type(cards)

        solved_tuple = (hand_type, cards, bid)

        # Find index for where to insert into 'solved_hands' (Need to keep it sorted)
        insert_index = 0
        for index, t in enumerate(solved_hands):
            insert_index = index
            if hand_type > t[0]:
                insert_index = index + 1
                continue
            if hand_type < t[0]:
                break

            card_val = 0
            other_val = 0
            for i in range(len(cards)):
                card_val = CARDS.index(cards[i])
                other_val = CARDS.index(t[1][i])
                if card_val == other_val:
                    continue
                break
            if card_val < other_val:
                insert_index = index + 1
                continue
            if card_val > other_val:
                break

        solved_hands.insert(insert_index, solved_tuple)
    total = 0
    for i, hand in enumerate(solved_hands):
        total += (i+1) * hand[2]
    return total


def p2(hands: list[tuple[str, int]]) -> int:
    CARDS = 'AKQT98765432J'
    solved_hands: deque[tuple[Hand_Types, str, int]] = deque()
    for hand in hands:
        cards, bid = hand
        hand_type = _solve_hand_type(cards, True)

        solved_tuple = (hand_type, cards, bid)

        # Find index for where to insert into 'solved_hands' (Need to keep it sorted)
        insert_index = 0
        for index, t in enumerate(solved_hands):
            insert_index = index
            if hand_type > t[0]:
                insert_index = index + 1
                continue
            if hand_type < t[0]:
                break

            card_val = 0
            other_val = 0
            for i in range(len(cards)):
                card_val = CARDS.index(cards[i])
                other_val = CARDS.index(t[1][i])
                if card_val == other_val:
                    continue
                break
            if card_val < other_val:
                insert_index = index + 1
                continue
            if card_val > other_val:
                break

        solved_hands.insert(insert_index, solved_tuple)
    total = 0
    for i, hand in enumerate(solved_hands):
        total += (i+1) * hand[2]
    return total


def main():
    hands = read_data()
    s1, s2 = p1(hands), p2(hands)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 251216224
# Part 2 solution: 250825971
