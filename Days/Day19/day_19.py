from re import findall


def read_data():
    file = 'Days/Day19/input.txt'
    with open(file, 'r') as f:
        return _parse_data(f.read().split('\n\n'))


def _parse_data(raw_data: list[str]) -> tuple[dict, list]:
    raw_workflows, raw_parts = raw_data
    workflows: dict[str, tuple[str, list[Rule]]] = {}

    for line in raw_workflows.split('\n'):
        name, raw_rules = line.split('{')
        rules = raw_rules[:-1].split(',')
        workflows[name] = (rules[-1], [])
        for rule in rules[:-1]:
            workflows[name][1].append(Rule(rule))

    parts: list[Part] = []
    for line in raw_parts.split('\n'):
        if line == '':
            continue
        nums = [int(num) for num in findall(r'\d+', line)]
        parts.append(Part(nums))

    return (workflows, parts)


class Part:
    chars = ['x', 'm', 'a', 's']
    x: int
    m: int
    a: int
    s: int

    def __init__(self, nums: list[int]) -> None:
        self.x = nums[0]
        self.m = nums[1]
        self.a = nums[2]
        self.s = nums[3]

    def total(self) -> int:
        return self.x + self.m + self.a + self.s


class Rule:
    label: str
    lt: bool
    value: int
    accept_dest: str

    def __init__(self, raw_str: str) -> None:

        self.lt = False
        split_char = '>'
        if '<' in raw_str:
            self.lt = True
            split_char = '<'

        left, accept = raw_str.split(':')
        self.accept_dest = accept

        label, value = left.split(split_char)
        self.label = label
        self.value = int(value)

    def valid(self, part: Part) -> bool:
        value = 0
        if self.label == 'x':
            value = part.x
        elif self.label == 'm':
            value = part.m
        elif self.label == 'a':
            value = part.a
        else:
            value = part.s
        if self.lt:
            if value < self.value:
                return True
            return False

        if value > self.value:
            return True
        return False


def p1(workflows: dict[str, tuple[str, list[Rule]]], parts: list[Part]) -> int:
    start_label = 'in'
    total = 0
    for part in parts:
        cur_label = start_label
        while True:
            next_label = ''
            for rule in workflows[cur_label][1]:
                if rule.valid(part):
                    next_label = rule.accept_dest
                    break
                next_label = workflows[cur_label][0]

            if next_label == 'A':
                total += part.total()
                break
            elif next_label == 'R':
                break
            cur_label = next_label
    return total


def p2(workflows: dict[str, tuple[str, list[Rule]]]) -> int:
    final_ranges_list: list[dict] = []
    ranges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
    queue: list[tuple[str, dict]] = [('in', ranges)]

    while len(queue) > 0:
        wf, part_ranges = queue.pop()
        cur_wf = workflows[wf]
        for rule in cur_wf[1]:
            alt_part_ranges = part_ranges.copy()

            if rule.lt:
                alt_part_ranges[rule.label] = (
                    alt_part_ranges[rule.label][0],
                    rule.value-1
                )
                part_ranges[rule.label] = (
                    rule.value,
                    part_ranges[rule.label][1]
                )
            elif not rule.lt:
                alt_part_ranges[rule.label] = (
                    rule.value + 1,
                    alt_part_ranges[rule.label][1]
                )
                part_ranges[rule.label] = (
                    part_ranges[rule.label][0],
                    rule.value
                )
            if rule.accept_dest in ['A', 'R']:
                if rule.accept_dest == 'A':
                    final_ranges_list.append(alt_part_ranges.copy())
            else:
                queue.append((rule.accept_dest, alt_part_ranges.copy()))

        if cur_wf[0] in ['A', 'R']:
            if cur_wf[0] == 'A':
                final_ranges_list.append(part_ranges.copy())
        else:
            queue.append((cur_wf[0], part_ranges.copy()))

    total = 0
    for ranges in final_ranges_list:
        cur_total = 1
        for a, b in ranges.values():
            cur_total *= (b-a) + 1
        total += cur_total
    return total


def main():
    workflows, parts = read_data()
    s1, s2 = p1(workflows, parts), p2(workflows)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 287054
# Part 2 solution: 131619440296497
