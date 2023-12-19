from re import findall


def read_data():
    file = 'Days/Day19/input.txt'
    with open(file, 'r') as f:
        return _parse_data(f.read().split('\n\n'))


def _parse_data(raw_data: list[str]) -> tuple[list, list]:
    raw_workflows, raw_parts = raw_data

    workflows: list[Workflow] = []
    for line in raw_workflows.split('\n'):
        name, rules = line.split('{')
        workflows.append(Workflow(name, rules[:-1]))

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

    def __str__(self) -> str:
        return f'{self.x}, {self.m}, {self.a}, {self.s}'


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

    def __str__(self) -> str:
        return f'{self.label}, {self.lt}, {self.value}, {self.accept_dest}'


class Workflow:
    name: str
    rules: list[Rule]
    reject: str

    def __init__(self, name: str, raw_rules: str) -> None:
        self.name = name
        raw_rules_list = raw_rules.split(',')
        self.reject = raw_rules_list[-1]
        self.rules = []
        for rule in raw_rules_list[:-1]:
            self.rules.append(Rule(rule))

    def next_destination(self, part: Part) -> str:
        for rule in self.rules:
            if rule.valid(part):
                return rule.accept_dest
        return self.reject


def p1(workflows: list[Workflow], parts: list[Part]) -> int:
    start_label = 'in'
    total = 0
    for part in parts:
        cur_label = start_label
        while True:
            wf_index = 0
            for i, wf in enumerate(workflows):
                if wf.name == cur_label:
                    wf_index = i
                    break
            next_label = workflows[wf_index].next_destination(part)
            if next_label == 'A':
                total += part.total()
                break
            elif next_label == 'R':
                break
            cur_label = next_label
    return total


def p2(workflows: list[Workflow], parts: list[Part]) -> int:
    return -1


def main():
    workflows, parts = read_data()
    s1, s2 = p1(workflows, parts), p2(workflows, parts)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 287054
# Part 2 solution:
