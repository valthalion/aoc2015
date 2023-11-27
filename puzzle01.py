def read_data():
    with open('puzzle01.in', 'r') as f:
        return next(f).strip()


moves = {'(': 1, ')': -1}


def part_1():
    floor = 0
    for c in read_data():
        floor += moves[c]
    return floor


def part_2():
    floor = 0
    for idx, c in enumerate(read_data(), start=1):
        floor += moves[c]
        if floor == -1:
            return idx
    return None
