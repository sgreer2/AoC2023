from __future__ import annotations
from copy import deepcopy
from enum import IntEnum
from math import lcm


def read_data():
    file = 'Days/Day20/input.txt'
    with open(file, 'r') as f:
        return _module_parse(f.read().split('\n')[:-1])


def _module_parse(lines: list[str]) -> dict[str, tuple[str, int, list[str], dict[str, Pulse]]]:
    modules = {}
    for line in lines:
        left, right = line.split(' -> ')
        key, m_type = '', ''

        if left == 'broadcaster':
            key = left
            m_type = left
        else:
            key = left[1:]
            m_type = left[0]

        modules[key] = (m_type, 0, [m for m in right.split(', ')], {})

    for key, module in modules.items():
        m_type, status, sub_mods, history = module
        if m_type == '&':
            for k, v in modules.items():
                _, _, s_mods, _ = v
                if key in s_mods:
                    history[k] = Pulse.LOW
            modules[key] = (m_type, status, sub_mods, history)
    return modules


class Pulse(IntEnum):
    LOW = 0
    HIGH = 1


def p1(modules: dict[str, tuple[str, int, list[str], dict[str, Pulse]]]) -> int:
    broadcaster = 'broadcaster'
    button_press_limit = 1_000
    low_count = 0
    high_count = 0
    queue = []

    for _ in range(button_press_limit):
        low_count += 1
        for mod in modules[broadcaster][2]:
            low_count += 1
            queue.append((Pulse.LOW, mod, broadcaster))

        while queue:
            pulse, mod_id, previous = queue.pop(0)
            if mod_id not in modules.keys():
                continue
            m_type, status, sub_mods, m_history = modules[mod_id]
            if m_type == '%':
                if pulse == Pulse.HIGH:
                    continue
                new_pulse = Pulse.LOW
                if status == 0:
                    new_pulse = Pulse.HIGH
                for sub_mod in sub_mods:
                    queue.append((new_pulse, sub_mod, mod_id))
                    if new_pulse == Pulse.HIGH:
                        high_count += 1
                    else:
                        low_count += 1
                status = 1 if status == 0 else 0
                modules[mod_id] = (m_type, status, sub_mods, m_history)
                continue
            if m_type == '&':
                if previous not in m_history.keys():
                    m_history[previous] = Pulse.LOW
                m_history[previous] = pulse
                if all(m_history.values()):
                    new_pulse = Pulse.LOW
                else:
                    new_pulse = Pulse.HIGH
                for sub_mod in sub_mods:
                    queue.append((new_pulse, sub_mod, mod_id))
                    if new_pulse == Pulse.HIGH:
                        high_count += 1
                    else:
                        low_count += 1
                modules[mod_id] = (m_type, status, sub_mods, m_history)
    return low_count * high_count


def _get_button_press_limit(modules: dict[str, tuple[str, int, list[str], dict[str, Pulse]]], start: str, end: str):
    modules = deepcopy(modules)
    button_presses = 0

    while True:
        queue: list[tuple[Pulse, str, str]] = []
        button_presses += 1
        for sub_mod in modules['broadcaster'][2]:
            if sub_mod == start:
                queue.append((Pulse.LOW, sub_mod, 'broadcaster'))
                break

        while queue:
            pulse, mod_id, previous = queue.pop(0)
            if mod_id not in modules.keys():
                continue
            m_type, status, sub_mods, m_history = modules[mod_id]
            if m_type == '%':
                if pulse == Pulse.HIGH:
                    continue
                new_pulse = Pulse.LOW
                if status == 0:
                    new_pulse = Pulse.HIGH
                for sub_mod in sub_mods:
                    queue.append((new_pulse, sub_mod, mod_id))
                status = 1 if status == 0 else 0
                modules[mod_id] = (m_type, status, sub_mods, m_history)
                continue
            if m_type == '&':
                if previous not in m_history.keys():
                    m_history[previous] = Pulse.LOW
                m_history[previous] = pulse
                if all(m_history.values()):
                    new_pulse = Pulse.LOW
                else:
                    new_pulse = Pulse.HIGH
                for sub_mod in sub_mods:
                    if sub_mod == end and new_pulse == Pulse.LOW:
                        return button_presses
                    queue.append((new_pulse, sub_mod, mod_id))
                modules[mod_id] = (m_type, status, sub_mods, m_history)


def p2(modules: dict[str, tuple[str, int, list[str], dict[str, Pulse]]]) -> int:
    target = 'rx'
    button_presses = []
    start_points = modules['broadcaster'][2]
    end_points = []

    for _, values in modules.items():
        _, _, sub_mods, sub_history = values
        if target in sub_mods:
            for key in sub_history.keys():
                end_points.append(key)

    pairs = []
    for node in start_points:
        queue = [node]
        found = False
        while found == False:
            cur_node = queue.pop(0)
            _, _, sub_mods, _ = modules[cur_node]
            for sub_node in sub_mods:
                if sub_node in end_points:
                    pairs.append((node, sub_node))
                    found = True
                    break
                queue.append(sub_node)

    for start, end in pairs:
        button_presses.append(_get_button_press_limit(modules, start, end))

    return lcm(*button_presses)


def main():
    modules = read_data()
    modules2 = deepcopy(modules)
    s1, s2 = p1(modules), p2(modules2)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 944750144
# Part 2 solution: 222718819437131
