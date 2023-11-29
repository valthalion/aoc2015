testing = False


def read_data():
    filename = 'puzzle17_test.in' if testing else 'puzzle17.in'
    with open(filename, 'r') as f:
        return tuple(int(line.strip()) for line in f)


def combinations(containers, target):
    def _combinations(target, idx, acc):
        if idx == len(containers):
            return
        container = containers[idx]
        yield from _combinations(target, idx + 1, acc)
        if container == target:
            yield (*acc, container)
        elif container < target:
            yield from _combinations(target - container, idx + 1, acc=(*acc, container))

    return tuple(_combinations(target, idx=0, acc=tuple()))


def part_1():
    containers = read_data()
    target = 25 if testing else 150
    combs = combinations(containers, target)
    return len(combs)


def part_2():
    containers = read_data()
    target = 25 if testing else 150
    combs = combinations(containers, target)
    min_num = min(len(comb) for comb in combs)
    return sum(1 for comb in combs if len(comb) == min_num)
