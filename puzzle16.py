readout = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

equal_keys = ('children', 'samoyeds', 'akitas', 'vizslas', 'cars', 'perfumes')
gt_keys = ('cats', 'trees')
lt_keys = ('pomeranians', 'goldfish')


def read_data():
    filename = 'puzzle16.in'
    sues = {}
    with open(filename, 'r') as f:
        for line in f:
            name, data = line.strip().split(': ', maxsplit=1)
            data = (pair.split(': ') for pair in data.split(', '))
            sues[name] = {k: int(v) for k, v in data}
    return sues


def match(sues, readout):
    return [
        sue for sue, data in sues.items() if all(readout[k] == v for k, v in data.items())
    ]


def match2(sues, readout):
    return [
        sue
        for sue, data in sues.items()
        if (
            all(readout[k] == v for k, v in data.items() if k in equal_keys) and
            all(v > readout[k] for k, v in data.items() if k in gt_keys) and
            all(v < readout[k] for k, v in data.items() if k in lt_keys)
           )
    ]


def part_1():
    sues = read_data()
    matching_sues = match(sues, readout)
    return matching_sues.pop()


def part_2():
    sues = read_data()
    matching_sues = match2(sues, readout)
    print(len(matching_sues))
    return matching_sues.pop()
