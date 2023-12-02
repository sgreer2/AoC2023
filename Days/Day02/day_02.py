
class Game:
    id: int
    rounds: list[list[tuple[int, str]]]
    p1_valid: bool
    p2_value: int

    def __init__(self, line: str) -> None:

        self._parse(line)
        self._p1_validate()
        self._p2_solve()

    def _parse(self, data: str) -> None:
        game_id, rounds = data.split(': ')

        self.id = int(game_id.replace('Game ', ''))
        self.rounds = []

        for round in rounds.split('; '):
            self.rounds.append([])
            for pair in round.split(', '):
                val, colour = pair.split(' ')
                self.rounds[-1].append((int(val), colour))

    def _p1_validate(self) -> None:
        limits = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        valid = True
        for round in self.rounds:
            for value, colour in round:
                if value > limits[colour]:
                    self.p1_valid = False
                    return

        self.p1_valid = valid

    def _p2_solve(self) -> None:
        colours = {}
        for round in self.rounds:
            for value, colour in round:
                if colour not in colours.keys():
                    colours[colour] = value
                    continue
                colours[colour] = max([value, colours[colour]])

        total = 1
        for c in colours.values():
            total *= c
        self.p2_value = total


def read_data():
    file = 'Days/Day02/input.txt'
    with open(file, 'r') as f:
        lines = f.read().split('\n')[:-1]
    return [Game(line) for line in lines]


def p1(games: list[Game]) -> int:
    total = 0
    for game in games:
        if game.p1_valid:
            total += game.id
    return total


def p2(games: list[Game]) -> int:
    total = 0
    for game in games:
        total += game.p2_value
    return total


def main():
    games = read_data()
    s1, s2 = p1(games), p2(games)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 2683
# Part 2 solution: 49710
