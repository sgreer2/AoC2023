from re import findall


class Map:
    maps: list

    def __init__(self, groups: list[list[str]]) -> None:
        temp = []
        for group in groups:
            temp.append(list())
            for line in group[1:]:
                if line == '':
                    break
                nums = [int(n) for n in findall(r'\d+', line)]
                t = [(nums[0], nums[0] + (nums[2])-1),
                     (nums[1], nums[1] + (nums[2])-1)]
                temp[-1].append(t)

        self.maps = temp

    def solve(self, val: int) -> int:
        for map in self.maps:
            for r in map:
                v_min, v_max = r[1]
                if val >= v_min and val <= v_max:
                    index = val - v_min
                    val = r[0][0] + index
                    break
        return val

    def r_solve(self, number: int) -> int:
        for map in self.maps[::-1]:
            for r in map:
                v_min, v_max = r[0]
                if number >= v_min and number <= v_max:
                    index = number - v_min
                    number = r[1][0] + index
                    break
        return number


def read_data():
    file = 'Days/Day05/input.txt'
    with open(file, 'r') as f:
        groups = [g.split('\n') for g in f.read().split('\n\n')]
    seeds = [int(n) for n in findall(r'\d+', groups[0][0])]
    maps = Map(groups[1:])
    return [seeds, maps]


def p1(seeds: list[int], maps: Map) -> int:
    locations = []
    for seed in seeds:
        locations.append(maps.solve(seed))
    return min(locations)


def p2(seeds: list[int], maps: Map) -> int:
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + (seeds[i+1])))
    cur_number = 0
    while True:
        result = maps.r_solve(cur_number)
        for seed_range in seed_ranges:
            if seed_range[0] <= result <= seed_range[1]:
                return cur_number
        cur_number += 1


def main():
    seeds, maps = read_data()
    s1, s2 = p1(seeds, maps), p2(seeds, maps)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 51580674
# Part 2 solution: 99751240
