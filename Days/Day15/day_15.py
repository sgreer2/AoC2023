
def read_data():
    file = 'Days/Day15/input.txt'
    with open(file, 'r') as f:
        return f.read().split('\n')[0]


def string_to_hash(string: str) -> int:
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value = value % 256

    return value


def p1(data: str) -> int:
    total = 0
    for line in data.split(','):
        total += string_to_hash(line)
    return total


def p2(data: str) -> int:
    boxes = dict()
    for i in range(256):
        boxes[i] = list()
    for line in data.split(','):
        if line[-1] == '-':
            string = line[:-1]
            box_id = string_to_hash(string)
            for i in range(len(boxes[box_id])):
                if boxes[box_id][i][0] == string:
                    boxes[box_id].pop(i)
                    break
            continue
        string, num = line.split('=')
        num = int(num)
        box_id = string_to_hash(string)
        index_in_there = -1
        for i in range(len(boxes[box_id])):
            if boxes[box_id][i][0] == string:
                index_in_there = i
                break
        if index_in_there == -1:
            boxes[box_id].append((string, num))
        else:
            boxes[box_id][index_in_there] = (string, num)

    total = 0
    for box, lenses in boxes.items():
        if lenses == []:
            continue
        box_values = []
        for i in range(len(lenses)):
            box_value = box + 1
            focal_length = lenses[i][1]
            box_value *= i+1
            box_value *= focal_length
            box_values.append(box_value)
        total += sum(box_values)
    return total


def main():
    data = read_data()
    s1, s2 = p1(data), p2(data)
    print(f'P1: {s1}')
    print(f'P2: {s2}')


if __name__ == '__main__':
    main()

# Part 1 solution: 519603
# Part 2 solution: 244342
