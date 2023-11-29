
def read_data():
    file = 'Day01/t_input.txt' if TESTING else 'Day01/input.txt'
    with open(file, 'r') as f:
        return f.read()


def p1(data):
    pass


def p2(data):
    pass


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


TESTING = True

if __name__ == '__main__':
    main()

# Part 1 solution:
# Part 2 solution:
