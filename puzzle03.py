from collections import defaultdict


values = {
    '^': 1j,
    'v': -1j,
    '<': -1,
    '>': 1
}


def read_data():
    with open('puzzle03.in', 'r') as f:
        for move in next(f).strip():
            yield values[move]


def part_1():
    presents = defaultdict(int)
    santa = 0
    presents[santa] += 1
    for move in read_data():
        santa += move
        presents[santa] += 1
    return len(presents)


def part_2():
    presents = defaultdict(int)
    santa, robosanta = 0, 0
    move_santa = True
    presents[santa] += 1
    for move in read_data():
        if move_santa:
            santa += move
            presents[santa] += 1
        else:
            robosanta += move
            presents[robosanta] += 1
        move_santa = not move_santa
    return len(presents)
