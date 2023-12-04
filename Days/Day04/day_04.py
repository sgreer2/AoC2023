from re import findall


def read_data():
    file = 'Days/Day04/input.txt'
    with open(file, 'r') as f:
        return parse(f.read().split('\n')[:-1])


def parse(array: list[str]):
    cards = []
    for line in array:
        nums = line.split(': ')[1]
        left, right = nums.split('|')
        cards.append([
            [int(l) for l in findall(r'\d+', left)],
            [int(r) for r in findall(r'\d+', right)]
        ])

    return cards


def p1(cards: list[list[list[int]]]) -> int:
    total = 0
    for c in cards:
        score = 0
        winning_nums, my_nums = c
        for win in winning_nums:
            if win in my_nums:
                if score == 0:
                    score += 1
                    continue
                score = score * 2

        total += score

    return total


def p2(cards: list[list[list[int]]]) -> int:
    scratch_cards = {x+1: 1 for x in range(len(cards))}

    cur_card = 1
    for card in cards:
        winning_nums, my_nums = card
        wins = 0

        for winner in winning_nums:
            if winner in my_nums:
                wins += 1

        for i in range(1, wins+1):
            scratch_cards[cur_card+i] += scratch_cards[cur_card]

        cur_card += 1
    return sum(scratch_cards.values())


def main():
    cards = read_data()
    s1, s2 = p1(cards), p2(cards)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 21088
# Part 2 solution: 6874754
