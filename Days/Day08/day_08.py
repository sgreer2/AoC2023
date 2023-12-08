from math import lcm


def read_data() -> tuple:
    file = 'Days/Day08/input.txt'
    with open(file, 'r') as f:
        lines = f.read().split('\n')[:-1]
    instructions = [0 if char == 'L' else 1 for char in lines[0]]
    nodes = {}
    for line in lines[2:]:
        nodes[line[0:3]] = (line[7:10], line[12:15])
    return (instructions, nodes)


def _get_steps(instructions: list[int], nodes: dict, start: str = 'AAA', part2: bool = False) -> int:
    cur_node = start
    steps = 0
    index = 0
    while True:
        if part2:
            if cur_node[2] == 'Z':
                return steps
        else:
            if cur_node == 'ZZZ':
                return steps
        cur_node = nodes[cur_node][instructions[index]]
        index += 1
        if index >= len(instructions):
            index = 0
        steps += 1


def p1(instructions: list[int], nodes: dict) -> int:
    return _get_steps(instructions, nodes)


def p2(instructions: list[int], nodes: dict) -> int:
    node_steps = []
    for node in nodes.keys():
        if node[2] == 'A':
            node_steps.append(_get_steps(instructions, nodes, node, True))
    return lcm(*node_steps)


def main():
    instructions, nodes = read_data()
    s1, s2 = p1(instructions, nodes), p2(instructions, nodes)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 16343
# Part 2 solution: 15299095336639
